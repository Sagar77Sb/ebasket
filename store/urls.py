
from django.urls import path
from .import views

urlpatterns=[
    path("-index",views.index,name="index1"),
   path("-register",views.regis,name="register1"),
   path("-login",views.loginn,name="logins"),
   path("logout",views.logoutt,name="logout"),
   path("-addcart/<int:pk>",views.cart,name="addcart"),
   path("-showcart",views.show_Cart,name="showcart"),
   path("delete/<int:proid>",views.delete,name='delete'),
   path("minuscart/<int:pid>",views.minus_cart,name="minuscart"),
   path("pluscart/<int:pid>",views.plus_cart,name="pluscart")
]