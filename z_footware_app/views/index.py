from django.views import View
from django.shortcuts import render,redirect
from z_footware_app.models.product import Product,Sizes
from z_footware_app.models.category import Category

class Index(View):
    def get(self,request):
        products=Product.objects.all()
        categories=Category.objects.all()
        sizes=Sizes.objects.all()
        category_id=request.GET.get('category_id')
        if category_id:
            products=Product.objects.filter(product_category=category_id)


        data={
            'products':products,
            'categories':categories,
            'sizes':sizes

        }
        return render(request,'index.html',data)

    def post(self,request):
        product_id = request.POST.get('product_id')
        cart=request.session.get('cart')
        remove=request.POST.get('remove')
        # size = request.POST.get('product_size')
        # str(size)


        # if product_id in cart:
        #     quantity = cart[product_id]
        #     # size= cart[product_id]
        #
        #     if remove:
        #         if quantity == 1:
        #             cart.pop(product_id)
        #         else:
        #             cart[product_id] = quantity - 1
        #     else:
        #         cart[product_id] = quantity + 1
        #         cart[product_id]['size'] = size
        #
        # else:
        #     if not remove:
        #         cart[product_id] = 1



        if cart:
            quantity=cart.get(product_id)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity - 1
                else:
                    cart[product_id]=quantity+1


            else:
                cart[product_id]=1

        else:
            cart = {}
            cart[product_id]=1


        request.session['cart']=cart
        print(cart)
        return redirect('home')



    def search(request):
        query = request.GET.get('query', '').strip()
        category_id = request.GET.get('category_id')

        # Always fetch all categories for the sidebar
        categories = Category.objects.all()

        # Handle product filtering
        if query:
            products = Product.objects.filter(product__icontains=query)
        elif category_id:
            products = Product.objects.filter(category_id=category_id)
        else:
            products = Product.objects.all()

        # Pass both categories and filtered products to the template
        return render(request, 'index.html', {
            'categories': categories,
            'products': products,
            'query': query,  # Pass query only if a search is performed
        })