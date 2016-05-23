from SyncAlot.Api import views
from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^product_update', views.product_update, name='product_update'),
]
