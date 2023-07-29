from django.db import models

class Categories(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    title= models.CharField(max_length=30)
    price=models.IntegerField(default='0')
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to='picture/')
    category=models.ForeignKey(Categories,on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title

