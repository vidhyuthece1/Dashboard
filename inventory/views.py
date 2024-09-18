from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

@login_required(login_url='user-login')
def index(request):
    order= Order.objects.all()
    products = Product.objects.all()
    workers_count = User.objects.all().count()
    products_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('inventory-index')
        
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'products': products,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count,
    }
    return render(request, 'inventory/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    products_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()
    
    context = {
        'workers': workers,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count,
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
    products_count = items.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            
            return redirect('inventory-product')
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form' : form,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count,
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
    orders = Order.objects.all()
    orders_count= orders.count()
    products_count = Product.objects.all().count()
    workers_count = User.objects.all().count()
    context={
        'orders' :orders,
        'workers_count' : workers_count,
        'products_count':products_count,
        'orders_count':orders_count,
    }
    return render(request, 'inventory/order.html',context)