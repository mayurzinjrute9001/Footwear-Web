from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from z_footware_app.models.product import Product
from z_footware_app.models.order import Customer_order
from z_footware_app.models.register import Register
from z_footware_app.models.payment import Payout
from time import time
from django.utils.decorators import method_decorator
from z_footware_app.middlewares.auth import auth_middleware
from z_footware.settings import *
import razorpay
client=razorpay.Client(auth=(KEY_ID,KEY_SECRET))


class Order(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer_id = request.session.get('id')
        customer = Register.objects.get(id=customer_id)

        # Retrieve all orders for the logged-in user
        orders = Customer_order.objects.filter(user=customer)

        # Calculate total amount for the cart (if needed for Razorpay order creation)
        cart = request.session.get('cart', {})
        products = Product.get_product_by_ids(list(cart.keys()))
        amount = sum([product.product_price * cart.get(str(product.id), 0) for product in products])

        action = request.GET.get('action')
        order = None
        payment = None
        error = None

        if action == 'create_payment':
            currency = "INR"
            notes = {"email": customer.email, "name": f'{customer.name}'}
            receipt = f"Z_Footwear-{int(time())}"
            try:
                order = client.order.create({
                    'receipt': receipt,
                    'notes': notes,
                    'amount': amount * 100,  # amount in paise
                    'currency': currency
                })
                payment = Payout.objects.create(
                    user=customer,
                    order_id=order.get('id'),
                )
                payment.product.set(products)
            except razorpay.errors.RazorpayError as e:
                error = str(e)

        context = {
            "orders": orders,  # Pass the orders to the template
            "products": products,
            "order": order,
            "payment": payment,
            "user": customer,
            "error": error,
        }
        return render(request, 'cart.html', context=context)

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('id')
        cart = request.session.get('cart', {})
        products = Product.get_product_by_ids(list(cart.keys()))

        # Create orders for each product in the cart
        for product in products:
            order = Customer_order(
                product=product,
                user=Register(id=customer_id),
                quantity=cart.get(str(product.id), 0),
                price=product.product_price,
                address=address,
                phone=phone
            )
            order.save()

        # Clear the cart after placing the order
        request.session['cart'] = {}
        return redirect('order')
