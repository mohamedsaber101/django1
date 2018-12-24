
from django.urls import path, re_path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('index', views.index),
    url(r'^$', views.index),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail),
    url(r'^album_title:(?P<album_title>[A-Za-z]+)basha/$', views.title),
 ]