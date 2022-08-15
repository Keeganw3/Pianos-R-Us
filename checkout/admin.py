from django.contrib import admin
from .models import Checkout, LineItems

class LineItemAdminInline(admin.TabularInline):
    model = LineItems
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    
    class Meta:
        verbose_name_plural = 'Checkout Orders'

    inlines = (LineItemAdminInline,)

    readonly_fields = ('order_id', 'order_total_cost', 
                       'checkout_date', 'original_cart',
                       'stripe_pid')

    fields = ('order_id', 'checkout_date', 'full_name',
              'email_address', 'phone_number', 'country',
              'postal_address', 'city', 'street_address_1',
              'street_address_2', 'county', 'order_total_cost',
              'original_cart', 'stripe_pid')

    list_display = ('order_id', 'checkout_date', 'full_name',
                    'order_total_cost',)

    ordering = ('-checkout_date',)

admin.site.register(Checkout, OrderAdmin)