from django.db import models
from django.contrib.auth.models import User
class Categories(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    title= models.CharField(max_length=30)
    price=models.IntegerField(default='0')
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to='image/')
    category=models.ForeignKey(Categories,on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title


class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    amount=models.IntegerField(default=0)
    total_amount=models.IntegerField(default=0)
    
    def total_cost(self):
        return self.quantity*self.product.price 
