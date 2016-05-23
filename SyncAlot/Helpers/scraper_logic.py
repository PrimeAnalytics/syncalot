import json
import urllib2
from urlparse import urlparse

from SyncAlot.models import Scraper, ProductUrl


def getXpaths(domain):
    xpaths = Scraper.objects.filter(host=domain).first()
    return xpaths


def checkProducts():
    products = ProductUrl.objects.all()
    for product in products:
        extractFields(product.url)
    return products


def extractFields(site):
    parsed_uri = urlparse(site)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri).strip("/")
    xpaths = getXpaths(domain)
    if xpaths:

        req = urllib2.Request(
            'https://extraction.import.io/query/extractor/' + xpaths.import_io_extractor_id + '?_apikey=' + xpaths.import_io_api_key + '&url=' + site)

        try:
            page = urllib2.urlopen(req)
            data = json.loads(page.read())
            values = parse(data, site)
            return values
        except urllib2.HTTPError, e:
            print e.fp.read()


def parse(data, site):
    if data:
        t = ProductUrl.objects.get(url=site)

        try:
            name = str(data['extractorData']['data'][0]['group'][0]['Name'][0]['text'])
            if len(name) > 0:
                t.name = name
        except:
            pass

        try:
            description = str(data['extractorData']['data'][0]['group'][0]['Description'][0]['text'])
            if len(description) > 0:
                t.description = description
        except:
            pass

        try:
            price = str(data['extractorData']['data'][0]['group'][0]['Price'][0]['text'])
            if len(price) > 0:
                t.price = float(filter(lambda x: x.isdigit(), price))
        except:
            pass
        try:
            stock = str(data['extractorData']['data'][0]['group'][0]['Stock'][0]['text'])
            if len(stock) > 0:
                t.stock = float(filter(lambda x: x.isdigit(), stock))
        except:
            pass
        t.save()
