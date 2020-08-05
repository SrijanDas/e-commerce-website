from .models import *
import json


def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES["cart"])
        # print(cart)
    except:
        cart = {}

    items = []
    order = {
        'get_cart_items': 0,
        'get_cart_total': 0,
    }

    cart_items = order['get_cart_items']

    for i in cart:
        try:
            cart_items += cart[i]["quantity"]
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quantity': cart[i]["quantity"],
                'get_total': total,
            }

            items.append(item)
            
        except:
            pass
    
    return {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        }


def cart_data(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    else:
        cookie_data = cookie_cart(request)
        items = cookie_data['items']
        order = cookie_data['order']
        cart_items = cookie_data['cart_items']
    return {'items': items, 'order': order, 'cart_items': cart_items}