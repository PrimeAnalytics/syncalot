from django.forms import ModelForm
from django.shortcuts import redirect, get_object_or_404

from SyncAlot.models import ProductUrl


class ProductUrlForm(ModelForm):
    class Meta:
        model = ProductUrl
        fields = ['url', 'product_code']
dffds


hfjhdsfhj
def product_url_create(request):
    post_values = request.POST.copy()
    form = ProductUrlForm(post_values)
    if form.is_valid():
        form.save()
        return redirect('/products')
    return redirect('/products', message=form.errors)


def product_url_update(request, pk):
    product = get_object_or_404(ProductUrl, pk=pk)
    form = ProductUrlForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/products')
    return redirect('/products')


def product_url_delete(request, pk):
    product = get_object_or_404(ProductUrl, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/products')
    return redirect('/products')
