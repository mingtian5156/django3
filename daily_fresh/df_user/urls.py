from django.conf.urls import url
from .views import *
# urlpattern = [
#     url(r'^index$',index),
# ]  na li cuo le 

urlpatterns = [
   
    url(r'^register/$', register),
    url(r'^register_handle/$', register_handle),
    url(r'^login/$', login),
    url(r'^login_handle/$', login_handle),
    url(r'^register_exist/$', register_exist),
    url(r'^info/$', info),
    url(r'^order/$', order),
    url(r'^site/$', site),
    url(r'^logout/$', logout),

    
    
    
]
