from django.db import models
from .category import Category

class Sizes(models.Model):
    size=models.IntegerField(default=7)

    def __str__(self):
        return str(self.size)

class Product(models.Model):
    product = models.CharField(max_length=30)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    product_description = models.CharField(max_length=30)
    product_price = models.FloatField(max_length=30)
    product_img = models.ImageField(upload_to="img/")
    product_size =models.ForeignKey(Sizes, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.product

    @staticmethod
    def get_product_by_ids(ids):
        return Product.objects.filter(id__in=ids)


