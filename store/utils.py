import json
from .models import *

from django.core.mail import EmailMessage

def cookieCart(request):
    try:
        # parsing cookies into a python dictionary
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('Cart:', cart)
    items = []
    order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping':False}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += 1

            product = Product.objects.get(id=i)
            price = product.price

            order['get_cart_total'] += price
            order['get_cart_items'] += 1

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                    'location': product.location,
                    'category': product.category
                }
            }

            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items':items}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # create a new order or get an order if it exists
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # query child objects by setting the parent value and then the child object
        # with all lowercase values and underscore set.all()
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items':items}

def guestOrder(request, data):
    name = data['form']['name']  
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email=email,
    )

    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
        )
    return customer, order

def sortData(sort, products):
    if (sort == 'low'):
        sorted_products = products.order_by('price')
    
    if (sort == 'high'):
        sorted_products = products.order_by('-price')

    if (sort == "relevant"):
        sorted_products = products

    return sorted_products

def filterData(params, products):
    sort = params.get('sort', 'relevant')
    products = sortData(sort, products)
        
    min_price = params['min']
    min_price = 0.0 if min_price == '' else float(min_price)
    max_price = params['max']
    max_price = 9999.99 if max_price == '' else float(max_price)

    filtered_products = []
    for p in products:
        if (p.price >= min_price and p.price <= max_price):
            filtered_products.append(p)

    return filtered_products

def sendEmail(data, request):
    name = data['form']['name'] if data['form']['name'] else str(request.user)
    email_id = data['form']['email'] if data['form']['email'] else request.user.email
    total = data['form']['total']
    message = 'Hello ' + name + '! Your order has been confirmed. You spent a total of $' + total + '.'
    msg = EmailMessage('TownDeals Confirmation!',
                       message, to=[email_id])
    msg.send()