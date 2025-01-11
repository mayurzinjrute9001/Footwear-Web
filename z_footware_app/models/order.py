from django.db import models
from .product import Product
from .register import Register
import datetime

class Customer_order(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(Register,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=30,default='')
    phone = models.CharField(max_length=20,default='')
    date = models.DateTimeField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    @staticmethod
    def get_order_by_customer(customer):
        return Customer_order.objects.filter(user=customer)
