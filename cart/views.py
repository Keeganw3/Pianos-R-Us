from django.shortcuts import render, redirect

# Create your views here.

def cart_view(request):
    """ A view that renders a user's cart items """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ A view that renders allows cart items to be incremented or decremented """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

    return render(request, 'cart/cart.html')