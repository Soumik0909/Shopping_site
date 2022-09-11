from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Offer


def index(request):
    products = Product.objects.all()
    offers=Offer.objects.all()
    return render(request, 'index.html', {'products': products, 'offers': offers})


