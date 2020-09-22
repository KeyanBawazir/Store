from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Product
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'view-products.html', {'products':products})
def show_time(request):
    now = timezone.now() 
    return render(request, 'time.html',{'time': now})   