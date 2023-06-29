from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

# Starting page for /products, convention naming: index
def index(request):
    # Product.objects.filter()
    # Product.objects.get()
    products = Product.objects.all()
    return render(request, 'index.html', 
                  {'products': products}) # Pass value into templates/index.html to Dynamically render value

    # return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Products')