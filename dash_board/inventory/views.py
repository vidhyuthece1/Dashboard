from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request,'inventory/index.html')

def staff(request):
    return render (request,'inventory/staff.html')

def product(request):
    return render(request,'inventory/product.html')
 
def order(request):
    return render(request, 'inventory/order.html')