from .cart import Cart

def cart(request):
    print(Cart(request))
    return {'cart': Cart(request)}