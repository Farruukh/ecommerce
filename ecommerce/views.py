from django.http import request
from django.shortcuts import render
from store.models import *

def index(request):
    products = Product.objects.filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'index.html', context)