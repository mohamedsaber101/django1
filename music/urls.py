
from django.urls import path, re_path
from django.conf.urls import url
from . import views
app_name = 'music'
urlpatterns = [
    path('index', views.index),
    url(r'^$', views.index, name="index"),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),

    url(r'^artist=(?P<artist>[a-z ]+)$', views.artist, name="artist"),

    url(r'^favorite/(?P<Album_id>[0-9]+)$', views.favorite, name="favorite")
 ]