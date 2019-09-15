from django.conf.urls import re_path
from django.views.generic import View

urlpatterns = [
    re_path(r'^simple/action/$', View.as_view(), name='simpleAction'),
]
