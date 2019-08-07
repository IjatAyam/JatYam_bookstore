from .cart import Cart


def cart(request):
    cart = Cart(request)
    cart.check()
    return {'cart': cart}
