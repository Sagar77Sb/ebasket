from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout




def index(request):
    products=Product.objects.all()
    category=Categories.objects.all()
    cat_id=request.GET.get('categories')
    if cat_id:
        product=Product.objects.filter(id=cat_id)
    else:
        products=Product.objects.all()
    d={'product':products,'category':category}
    return render(request,"index.html",d)

def regis(request):
    if request.method=='POST':
        obj=RegisterForm(request.POST)
        obj.save()
        return redirect("/Ebasket-login")
    else:
        d={'form':RegisterForm}
        return render(request,'register.html',d)
    

def loginn(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        passwd=request.POST.get("password")
        user=authenticate(request,username=uname,password=passwd)
        if user is not None:
            request.session["id"]=user.id 
            print(request.session.get("id"))
            login(request,user)
            return redirect("/")
        else:
            d={'form':LoginForm}
            return render(request,'login.html',d)
    else:
            d={'form':LoginForm}
            return render(request,'login.html',d)

def logoutt(request):
    logout(request)
    return redirect("/")  

def cart(request,pk):
    user_id=request.session.get("id")
    user=request.user
    product=Product.objects.get(id=pk)
    Cart(user=user,product=product).save()
    return redirect("/")

def show_Cart(request):
     ids=request.session.get("id")

     obj=Cart.objects.filter(user=ids)
     amount=0
     value=0
     for p in obj:
            
            value= p.quantity * p.product.price
            amount= value + amount
     total_amount= amount +50
  
     d={'data':obj,'total_amount':total_amount,'amount':amount}
     return render(request,'cart.html',d)

def plus_cart(request,pid):
    if request.method=="GET":
        c=Cart.objects.get(id=pid)
        c.quantity +=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        for p in cart:
            amount=0
            value= p.quantity * p.product.price
            amount= value + amount
        total_amount= amount + 50
        data={
            "quantity":c.quantity,
            "amount":c.amount,
            "totalamount":c.total_amount
        }
        return redirect("/Ebasket-showcart")

def minus_cart(request,pid):
    if request.method=="GET":
        c=Cart.objects.get(id=pid)
        c.quantity -=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        for p in cart:
            amount=0
            value= p.quantity * p.product.price
            amount= value + amount
        total_amount= amount + 50
        data={
            "quantity":c.quantity,
            "amount":c.amount,
            "totalamount":c.total_amount
        }
        return redirect("/Ebasket-showcart")




def delete(request,proid):
    obj=Cart.objects.get(id=proid)
    obj.delete()
    return redirect("/Ebasket-showcart")
