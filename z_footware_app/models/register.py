from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.IntegerField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_user_by_id(user_id):
        return Register.objects.filter(id=user_id)