import json
import time

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from products.models import Product
from accounts.models import UserAccount
from .models import Checkout, LineItems





class StripeWH_Handler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_generic_event(self, event):
        """
        Handles unknown/unexpected/generic webhook events
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_successful_payment_intent(self, event):
        """
        Handles successful payment intent webhooks from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        order_total_cost = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        account = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            account = UserAccount.objects.get(user__username=username)
            if save_info:
                account.default_phone_number = shipping_details.phone
                account.default_country = shipping_details.address.country
                account.default_postal_address = shipping_details.address.postal_address
                account.default_city = shipping_details.address.city
                account.default_street_address_1 = shipping_details.address.line_1
                account.default_street_address_2 = shipping_details.address.line_2
                account.default_county = shipping_details.address.state
                account.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Checkout.objects.get(
                    full_name__iexact=shipping_details.name,
                    email_address__iexact=billing_details.email_address,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_address,
                    city__iexact=shipping_details.address.city,
                    street_address_1__iexact=shipping_details.address.line_1,
                    street_address_2__iexact=shipping_details.address.line_2,
                    county__iexact=shipping_details.address.state,
                    order_total_cost=order_total_cost,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Checkout.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | \
                     SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Checkout.objects.create(
                    full_name=shipping_details.name,
                    user_account=account,
                    email_address=billing_details.email_address,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_address,
                    city=shipping_details.address.city,
                    street_address_1=shipping_details.address.line_1,
                    street_address_2=shipping_details.address.line_2,
                    county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        line_items = LineItems(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        line_items.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: \
            Created order in webhook',
            status=200)

    def handle_failed_payment_intent(self, event):
        """
        Handles failed payment intent webhooks from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
