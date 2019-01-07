from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404

from .models import *
from django.shortcuts import render

def index(request):
    all = Album.objects.all()
    cont = {"albums": all }
    return render(request, 'music/index.html', cont )


'''
def detail(request, album_id):
    try:
        exist = Album.objects.get(id=album_id)
        for song in exist.song_set.all():
            print (song.song_title)

        cont = {"sample": exist , "songs": exist.song_set.all()}

        return render(request, "music/album.html", cont)
    except:

        raise Http404("Doesn't Exist")
'''
def detail(request, album_id):
    a = get_object_or_404(Album,  pk=album_id)
    return render(request, 'music/album.html', {"sample": a, "songs": a.song_set.all()})


def title(request,  album_title):
    return HttpResponse('<html><head><title> Saber developer as  title </title></head><body><h1>Hello its Me saber DEVELOPER</h1><h2>Here are the details of Album title: ' + str(album_title) + '</h2></body></html>')

def artist(requset, artist):

    cont = {"artist" : artist}

    return  render(requset, 'music/artists.html', cont)


def favorite(request, Album_id):
    a = get_object_or_404(Album, pk=Album_id)
    song = a.song_set.get(pk=request.GET['song'])
    song.is_favorite = True
    song.save()
    return HttpResponse(request.GET['song'] + '  favorited!!')

