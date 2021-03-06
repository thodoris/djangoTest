from cart.cart import Cart
import drugs.cacheService as cacheService


def baseurl(request):
    """
    Return a BASE_URL template context for the current request.
    """
    if request.is_secure():
        scheme = 'https://'
    else:
        scheme = 'http://'

    return {'BASE_URL': scheme + request.get_host(), }

def store_context(request):
    def inner():
        cart = Cart(request)
        cart_is_empty = cart.count() == 0
        drug_categories = cacheService.get_drug_categories()
        return {
            'cart': cart,
            'cart_is_empty': cart_is_empty,
            'drug_categories' : drug_categories

        }
    return {'store_context': inner}
