from django.shortcuts import redirect, render
from shop.form import CustomUserCreationForm
from .models import *
from django.contrib import messages



def home(request) :
    products = Product.objects.filter(trending=1)
    return render(request, 'shop/index.html', {'products':products})

def register(request) :
    form = CustomUserCreationForm()
    return render(request, 'shop/register.html',{'form':form})


def collection(request) :
    category = Category.objects.filter(status=0)
    return render(request, 'shop/collection.html', {'category':category})

def collectionview(request,name) :
    if (Category.objects.filter(name=name, status=0)):
        products = Product.objects.filter(Category__name=name)
        return render(request, 'shop/products/index.html',{'products':products, 'category_name':name})
    else:
        messages.warning(request, "No such category found")
        return redirect('collection')

def product_details(request, cname, pname) :
    if (Category.objects.filter(name=cname, status=0)):
        if (Product.objects.filter(name=pname, status=0)):
            products = Product.objects.filter(name=pname, status=0).first()
            return render(request, 'shop/products/product_details.html',{'products':products})
        else:
            messages.error(request, "No such product found")
            return redirect('collection')
    else:
        messages.error(request,"No such category found")
        return redirect('collection')
    
