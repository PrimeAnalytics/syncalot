from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404

from SyncAlot.models import Scraper


class ProductForm(ModelForm):
    class Meta:
        model = Scraper
        fields = ['host', 'import_io_api_key','import_io_extractor_id']


@login_required
def scraper_list(request):
    scrapers = Scraper.objects.all()
    data = {}
    data['object_list'] = enumerate(scrapers)
    return render(request, 'admin/scraper.html', data)


def scraper_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('/scraper')


def scraper_update(request, pk):
    product = get_object_or_404(Scraper, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
    return redirect('/scraper')


def scraper_delete(request, pk):
    product = get_object_or_404(Scraper, pk=pk)
    if request.method == 'POST':
        product.delete()
    return redirect('/scraper')
