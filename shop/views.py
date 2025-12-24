from django.shortcuts import render
from .models import *


def home(request) :
    return render(request, 'shop/index.html')

def register(request) :
    return render(request, 'shop/register.html')

def collection(request) :
    category = Category.objects.filter(status=0)
    return render(request, 'shop/collection.html', {'category':category})


