from django.conf.urls import url

from SyncAlot.Scrapers import views

urlpatterns = [
    url(r'^$', views.scraper_list, name='scraper_list'),
    url(r'^new$', views.scraper_create, name='scraper_new'),
    url(r'^edit/(?P<pk>\d+)$', views.scraper_update, name='scraper_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.scraper_delete, name='scraper_delete'),
]
