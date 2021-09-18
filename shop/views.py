from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import product,category
from math import ceil
# Create your views here.
def index(request):
    pd=product.objects.all()
    cat=category.objects.all()
    # print(len(cat))
    all_cat_product=product.objects.raw('select * from products group by category')[0]
    print(all_cat_product)
    # all_cat_product=[]
    for i in cat:
        cat_product=product.objects.filter(category=cat)
        # all_cat_product[i]=cat_product
        all_cat_product.append([i,cat_product])
    # for i in all_cat_product:
    #     print(i)   
    params={'category':cat,'all_product':all_cat_product}
    return render(request,'shop/home.html')
def about(request):
    return HttpResponse("We are at about")
def contact(request):
    return HttpResponse("We are at contact")
def tracker(request):
    return HttpResponse("We are at tracker")
def search(request):
    return HttpResponse("We are at search")
def productView(request):
    return HttpResponse("We are at product view")
def checkout(request):
    return HttpResponse("We are at checkout")