
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^$', admin.site.urls)
]
#change