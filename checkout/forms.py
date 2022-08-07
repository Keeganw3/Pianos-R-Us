from django import forms
from .models import Checkout


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ('full_name', 'email_address', 'phone_number',
                  'street_address_1', 'street_address_2',
                  'city', 'postal_address', 'country', 'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes while removing auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postal_address': 'Postal Code',
            'city': 'Town or City',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False