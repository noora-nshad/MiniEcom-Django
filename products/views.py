# from django.shortcuts import render,get_object_or_404
# from .models import Product
# from django.contrib.auth.decorators import login_required
# # Create your views here.

# @login_required
# def product_list(request):
#     products=Product.objects.all()
#     return render(request,'products/product_list.html',{'products':products})

# @login_required
# def product_detail(request,id):
#     product=get_object_or_404(Product,id=id)
#     return render(request,'products/product_detail.html',{'product':product})

from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .forms import ProductForm
from django.shortcuts import redirect

# Create your views here.

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


@login_required
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    # Recently Viewed Products (Session)
    recent = request.session.get('recent', [])

    if id in recent:
        recent.remove(id)

    recent.insert(0, id)

    recent = recent[:5]      # Keep only last 5 products

    request.session['recent'] = recent

    return render(request, 'products/product_detail.html', {'product': product})

@api_view(['GET'])
def product_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "products/product_form.html", {"form": form})


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "products/product_form.html", {"form": form})


@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "products/delete_product.html", {"product": product})