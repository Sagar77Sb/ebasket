from django.shortcuts import render,redirect
from .models import *

def index(request):
    products=Product.objects.all()
    category=Categories.objects.all()
    d={'product':products,'category':category}
    return render(request,"index.html",d)

