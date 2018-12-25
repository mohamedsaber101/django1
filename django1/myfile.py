from music.models import Album

a = Album.objects.get(pk=4)
a.artist