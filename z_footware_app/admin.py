from django.contrib import admin
from z_footware_app.models.register import Register
from .models.product import Product
from .models.product import Sizes
from .models.category import Category
from .models.order import Customer_order
from .models.payment import Payout
#  Register your models here.
admin.site.register(Register)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sizes)
admin.site.register(Customer_order)
admin.site.register(Payout)




