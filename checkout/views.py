from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import CheckoutForm
from .models import Checkout, LineItems
from products.models import Product
from cart.contexts import cart_contexts

import stripe	

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
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
            order = checkout_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        line_items = LineItems(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        line_items.save()
        
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag couldn't be found in our database."
                        "Email us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_id]))
        else:
            messages.error(request, 'There was an error with your form. \ Please double check your information.')
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
    checkout_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
	

def checkout_success(request, order_id):
    """
    Emails the customer after a successful checkout
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Checkout, order_id=order_id)
    messages.success(request, f'Order successfully processed! \ Your order number is {order_id}. A confirmation \ email will be sent to {order.email_address}.')
    if 'cart' in request.session:
        del request.session['cart']
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
