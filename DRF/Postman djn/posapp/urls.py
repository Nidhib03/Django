from django.urls import re_path as url
from .views import RestfileView

urlpatterns = [
    url(r'^upload/$', RestfileView.as_view(), name='file-upload'),
]