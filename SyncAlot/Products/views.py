from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404

from SyncAlot.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_code', 'category', 'brand', 'email']


@login_required
def product_list(request):
    products = Product.objects.all()
    data = {}
    data['object_list'] = products
    return render(request, 'customer/products.html', data)


def product_create(request):
    post_values = request.POST.copy()
    post_values['email'] = request.user.email
    form = ProductForm(post_values)
    if form.is_valid():
        form.save()
        return redirect('/products')
    return redirect('/products', message=form.errors)


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/products')
    return redirect('/products')


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/products')
    return redirect('/products')
