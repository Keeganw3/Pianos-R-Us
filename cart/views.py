from django.shortcuts import render, redirect, reverse, HttpResponse


def cart_view(request):
    """ A view that renders a user's cart items """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ A view that allows cart items to be increased or decreased """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ A view that allows the user to change the quantity of
        items their ordering """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('cart_view'))


def remove_from_cart(request, item_id):
    """ A view that allows the user to remove items from their cart """

    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

        