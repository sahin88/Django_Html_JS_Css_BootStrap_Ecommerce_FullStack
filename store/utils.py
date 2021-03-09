import json
from .models import Product


def nonuser(request):
    order = {}
    itemk = []
    try:
        cart = json.loads(request.COOKIES['cart'])
    except Exception as ee:
        cart = {}
    print("cart", cart)
    total_price_list = []
    total_amiount_list = []
    for product_id, quantities in cart.items():

        product = Product.objects.get(id=int(product_id))

        item = {"product": {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'imageUrl': product.imageUrl
        },
            'totalPrice': float(product.price)*float(quantities['quantity']),
            'quantity': int(quantities['quantity'])

        }
        if product.digital:
            order['shipping'] = False

        total_amiount_list.append(int(quantities['quantity']))
        total_price_list.append(
            float(product.price)*float(quantities['quantity']))
        itemk.append(item)

    order = {'totalPrice': sum(total_price_list), 'totalItem': sum(
        total_amiount_list)}

    context = {'items': itemk,
               'orders': order}
    return context
