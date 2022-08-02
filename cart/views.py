from django.shortcuts import render

# Create your views here.

def cart_view(request):
    """ A view that renders a user's cart items """

    return render(request, 'cart/cart.html')