from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('order_history/<order_id>', views.order_history, name='order_history'),
]