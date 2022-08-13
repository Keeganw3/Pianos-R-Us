from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings	

from .forms import CheckoutForm	
from cart.contexts import cart_contexts	

import stripe	

def checkout(request):	
    stripe_public_key = settings.STRIPE_PUBLIC_KEY	
    stripe_secret_key = settings.STRIPE_SECRET_KEY	
    

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

    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
	    'stripe_public_key': stripe_public_key,	
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)