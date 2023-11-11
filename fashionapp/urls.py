from django.urls import path

from fashionapp import views

urlpatterns = [
    path('',views.homepage,name='home'), #for home page
    path('productpage',views.productpage,name='product'),#for product page
    path('cartpage',views.cartpage,name='cart'), #for cart page

    path('paymentpage',views.paymentpage,name='payment'), #for payment page
    path('orderedpage',views.orderpage,name='order'), #for order page

    path('home',views.home)
]