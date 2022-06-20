from django.shortcuts import render

from .models import Category, Product

# Create your views here.
def product_list(request, category_slug=None):
    """List all the products or filter products by a given category."""

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        # filter products by a given category
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    data = {'category': category, 'categories': categories, 'products': products}

    return render(request, 'shop/product/list.html', data)

def product_detail(request, id, slug):
    """Retrives and displays a single product."""

    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    data = {'product': product}

    return render(request, 'shop/product/detail.html', data)
