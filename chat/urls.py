from django.contrib import admin
from django.conf.urls import url
from .views import index, room, test
from django.urls import re_path

urlpatterns = [
    url(r'^$', index),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
    re_path(r'^test/(?P<id>.*)/$', test)
]
