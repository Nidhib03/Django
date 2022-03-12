from django.urls import re_path as url
from resapp import views 
 
urlpatterns = [ 
    url(r'^api/resapp$', views.reapp_list),
    url(r'^api/resapp/(?P<name>[a-z]+)$', views.reapp_detail),
    url(r'^api/info$', views.reapp_list_info),
]