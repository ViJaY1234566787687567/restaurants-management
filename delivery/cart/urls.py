from django.contrib import admin
from django.urls import path,include
from cart import views
app_name="cart"


urlpatterns = [
   path('addtocart/<n>',views.addtocart,name="addtocart"),
   path('cartview',views.cartview,name="cartview"),
   path('cart_remove/<n>',views.cart_remove,name="cart_remove"),
   path('full_remove/<n>',views.full_remove,name="full_remove"),
   path('orderform',views.orderform,name="orderform"),
   path('orderview', views.orderview, name="orderview"),

   ]