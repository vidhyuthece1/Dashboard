from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.index,name="inventory-index"),
    path('staff/',views.staff,name='inventory-staff'),
    path('staff/detail/<int:pk>',views.staff_detail,name='inventory-staff-detail'),
    path('product/',views.product, name='inventory-product'),
    path('product/delete/<int:pk>/',views.product_delete,name='inventory-product-delete'),
    path('product/update/<int:pk>/',views.product_update,name='inventory-product-update'),
    path('order/',views.order,name='inventory-order'),
]
