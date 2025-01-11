from django.db import models
from .product import Product
from .register import Register

class Payout(models.Model):
    order_id=models.CharField(max_length=50,null=False)
    payment_id=models.CharField(max_length=50)
    product=models.ManyToManyField(Product)
    user=models.ForeignKey(Register,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)