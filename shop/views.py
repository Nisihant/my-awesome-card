from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import product,category
from math import ceil
# Create your views here.
def index(request):
    context = {}
    prod_by_category = {}
    for i in product.objects.all():
        try:
            prod_by_category[i.category.category_name].append(i)
        except:
            prod_by_category[i.category.category_name] = []
            prod_by_category[i.category.category_name].append(i)
            
    context["products"] = prod_by_category
    return render(request, "shop/home.html", context)

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    p=request.POST.get("product_id")
    # p=int(p)
    prod=product.objects.get(product_id=p)
    print(prod)
    return  render(request, "shop/shop_product_detail.html",{"prod":prod})

def checkout(request):
    return HttpResponse("We are at checkout")