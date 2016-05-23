"""SyncAlot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import SyncAlot.Api.urls
import SyncAlot.Product_Url.urls
import SyncAlot.Products.urls
import SyncAlot.Scrapers.urls
import views

urlpatterns = [
    url(r'^$', views.index, {}, 'index'),
    url(r'^pricing', views.pricing, {}, 'pricing'),
    url(r'^dashboard', views.dashboard, {}, 'dashboard'),
    url(r'^products/', include(SyncAlot.Products.urls)),
    url(r'^product_url/', include(SyncAlot.Product_Url.urls)),
    url(r'^scraper/', include(SyncAlot.Scrapers.urls)),
    url(r'^api/', include(SyncAlot.Api.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', 'django.contrib.auth.views.login', {
    'template_name': 'login.html'
})
]
