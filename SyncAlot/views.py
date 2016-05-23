from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from SyncAlot.models import Product
from SyncAlot.models import ProductUrl
from urlparse import urlparse
from operator import itemgetter
from itertools import groupby


def index(request):
    context = {}
    return render(request, 'home/index.html', context)


def pricing(request):
    context = {}
    return render(request, 'home/pricing.html', context)


@login_required
def dashboard(request):

    index_data =[]
    product_data = []
    products = Product.objects.all()

    for product in products:
        total = 0
        count = 0
        urls = product.producturl_set.all()
        for url in urls:
            parsed_uri = urlparse(url.url)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri).strip("/")
            product_data.append({"host":domain, "price":url.price})
            total += url.price
            count += 1
        index_data.append({ "avg_price": total/count, "product_code":product.product_code })

    counts = []
    ordered_data = sorted(product_data, key=itemgetter('host'))
    for region, group in groupby(ordered_data, key=itemgetter('host')):
        group_list = list(group)
        total = sum(int(purl['price']) for purl in group_list)
        counts.append({"host":region, "price":total})


    return render(request, 'customer/dashboard.html', {"data":index_data,"product_data":counts})
