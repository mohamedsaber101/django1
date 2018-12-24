from django.shortcuts import render

# Create your views here.
from django import http
from django.urls import include
from .models import *
999

def index(request):
    all = Album.objects.all()
    html= '<html><head><title> Saber developer as  title </title></head><body>'
    for album in all:
        url = '/music/' + str(album.id) + '/'
        html += '<h1> <a href="' + url + '">' + album.album_title + '</a></h1></br>'

    html += ' </body></html>'


    return http.HttpResponse(html)

def detail(request, album_id):
    return http.HttpResponse('<html><head><title> Saber developer as  title </title></head><body><h1>Hello its Me saber DEVELOPER</h1><h2>Here are the details of Album: ' + str(album_id) + '</h2></body></html>')

def title(request, album_title):
    return http.HttpResponse('<html><head><title> Saber developer as  title </title></head><body><h1>Hello its Me saber DEVELOPER</h1><h2>Here are the details of Album title: ' + str(album_title) + '</h2></body></html>')
