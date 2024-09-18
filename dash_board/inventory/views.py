from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.contrib.auth.models import User
# Create your views here.

@login_required
def index(request):
    return render (request,'inventory/index.html')

@login_required
def staff(request):
    workers = User.objects.all()
    context = {
        'workers': workers
    }
    return render (request,'inventory/staff.html',context)

@login_required
def staff_detail(request,pk):
    workers = User.objects.get(id = pk)
    context={
        'workers' : workers,
    }
    return render(request,'inventory/staff_detail.html',context)

@login_required
def product(request):
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory-product')
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'inventory/product.html',context)

@login_required
def product_delete(request,pk):
    item = Product.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory-product')
    return render(request,'inventory/product_delete.html')

@login_required
def product_update(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'inventory/product_update.html', context)

@login_required
def order(request):
    return render(request, 'inventory/order.html')