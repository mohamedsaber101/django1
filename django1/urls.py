
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

urlpatterns = [
    re_path(r'^$', include('music.urls')),
    path('admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
]
#change