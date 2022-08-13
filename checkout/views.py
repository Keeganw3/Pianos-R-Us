from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import CheckoutForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': 'pk_test_51LK40UI31Ly6KbPUKCD8jZOxuCk5Eqjr84wqz8ZFIMWVl61Chv7Mo8kDXjy3cCSO7nKlWs1btlOmnHiiE4ecFkT200mTgPy9RO',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)