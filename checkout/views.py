import json

from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe

from products.models import Product
from accounts.models import UserAccount
from accounts.forms import UserAccountForm
from cart.contexts import cart_contexts

from .forms import CheckoutForm
from .models import Checkout, LineItems


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry, your payment can't be \
            processed at the moment. Please try again later.")
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postal_address': request.POST['postal_address'],
            'city': request.POST['city'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'county': request.POST['county'],
        }
        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            order = checkout_form.save(commit=False)

            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        line_items = LineItems(
                            checkout=order,
                            product=product,
                            quantity=item_data,
                        )
                        line_items.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart couldn't be found \
                        in our database." "Email us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_id]))
        else:
            messages.error(request, 'There was an error with your form. \
            Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart right now")
            return redirect(reverse('products'))

        current_cart = cart_contexts(request)
        total = current_cart['order_total_cost']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                account = UserAccount.objects.get(user=request.user)
                checkout_form = CheckoutForm(initial={
                    'full_name': account.user.get_full_name(),
                    'email': account.user.email,
                    'phone_number': account.default_phone_number,
                    'country': account.default_country,
                    'postal_address': account.default_postal_address,
                    'city': account.default_city,
                    'street_address_1': account.default_street_address_1,
                    'street_address_2': account.default_street_address_2,
                    'county': account.default_county,
                })
            except UserAccount.DoesNotExist:
                checkout_form = CheckoutForm()
        else:
            checkout_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you \
        forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_id):
    """
    Handles successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Checkout, order_id=order_id)

    if request.user.is_authenticated:
        account = UserAccount.objects.get(user=request.user)
        # Attach the user's account to the order
        order.user_account = account
        order.save()

        # Save the user's info
        if save_info:
            account_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postal_address': order.postal_address,
                'default_city': order.city,
                'default_street_address_1': order.street_address_1,
                'default_street_address_2': order.street_address_2,
                'default_county': order.county,
            }
            user_account_form = UserAccountForm(account_data, instance=account)
            if user_account_form.is_valid():
                user_account_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order id is {order_id}. A confirmation \
        email will be sent to {order.email_address}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
