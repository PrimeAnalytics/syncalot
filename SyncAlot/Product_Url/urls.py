from django.conf.urls import url

from SyncAlot.Product_Url import views

urlpatterns = [
    url(r'^new$', views.product_url_create, name='product_new'),
    url(r'^edit/(?P<pk>\d+)$', views.product_url_update, name='product_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.product_url_delete, name='product_delete'),
]
