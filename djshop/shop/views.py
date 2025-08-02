from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Category, Product


def shop(request):

    all_products = Product.objects.all()
    context = {
        "my_products": all_products
    }

    return render(request, template_name="shop/shop.html", context=context)


def categories(request):

    all_categories = Category.objects.all()

    return {"all_categories": all_categories}


def list_category(request, category_slug=None):

    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    context = {
        "category": category,
        "products": products
    }

    return render(request, template_name="shop/list-category.html", context=context)


def product_info(request, product_slug):

    product = get_object_or_404(Product, slug=product_slug)

    context = {
        "product": product
    }

    return render(request, "shop/product-info.html", context)
