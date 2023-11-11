from django.shortcuts import render, redirect


# Create your views here.
def homepage(request):
    return render(request,'homepage.html')


def productpage(request):
    return render(request,'product.html')


def cartpage(request):
    return render(request,'cart.html')


def paymentpage(request):
    return render(request,'payment.html')


def orderpage(request):
    return render(request,'ordered.html')


def home(request):
    return redirect('home')