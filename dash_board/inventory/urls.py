from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.index,name="inventory-index"),
    path('staff/',views.staff,name='inventory-staff'),
    path('product/',views.product, name='inventory-product'),
    path('order/',views.order,name='inventory-order'),
]
