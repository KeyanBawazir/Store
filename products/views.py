from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products':products})
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    render(request,'product_details.html',{'product': product})
def show_time(request):
    now = timezone.now() 
    return render(request, 'time.html',{'time': now})   