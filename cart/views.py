from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import cart, cartitem
from products.models import Product





@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_obj, created = cart.objects.get_or_create(user=request.user)
    item, created = cartitem.objects.get_or_create(cart=cart_obj,product=product)
    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart_obj = cart.objects.get(user=request.user)
    items = cartitem.objects.filter(cart=cart_obj)
    total = sum(item.total_price() for item in items)
    return render(request, "cart/cart_detail.html", {"items": items,"total": total})


@login_required
def increase_quantity(request, item_id):
    item = get_object_or_404(cartitem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('cart_detail')


@login_required
def decrease_quantity(request, item_id):
    item = get_object_or_404(cartitem, id=item_id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()

    return redirect('cart_detail')


@login_required
def remove_item(request, item_id):
    item = get_object_or_404(cartitem, id=item_id)
    item.delete()
    return redirect('cart_detail')