from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_display, name='products'),
    path('<int:product_id>/', views.product_view, name='product_view'),
    path('add/', views.add_product, name='add_product'),
]