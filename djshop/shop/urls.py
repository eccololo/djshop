from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('product/<slug:slug>', views.product_info, name="product-info"),
] 
