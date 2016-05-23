from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse

from SyncAlot.Helpers.scraper_logic import checkProducts
from SyncAlot.models import Product


@login_required
def product_list(request):
    products = Product.objects.all()
    products_serialized = serializers.serialize('json', products, fields=('name', 'product_code', 'category', 'brand'))
    return JsonResponse(products_serialized, safe=False)


@login_required
def product_update(request):
    products = checkProducts()
    products_serialized = serializers.serialize('json', products)
    return JsonResponse(products_serialized, safe=False)
