from django.conf.urls import url
from .views import * 


urlpatterns = [
    url(r'^$',cart),
    url(r'^add(\d+)_(\d+)/$',add),
    url(r'^edit(\d+)_(\d+)/$',edit),
    url(r'^delete(\d+)/$',delete),
]
   