from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import LineItems

@receiver(post_save, sender=LineItems)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    print('update')
    instance.checkout.update_total()

@receiver(post_delete, sender=LineItems)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    print('delete')
    instance.checkout.update_total()