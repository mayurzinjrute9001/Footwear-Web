from django.shortcuts import render
from django.views import View
from z_footware_app.models.product import Product
from z_footware_app.models.register import Register


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products=Product.get_product_by_ids(ids)
        print(products)
        user_id=request.session.get('id')
        users=Register.get_user_by_id(user_id)

        return render(request, 'cart.html',{'products':products,'users':users})
