from music.models import Album, Song

a = Album.objects.get(pk=4)
a.artist

a.song_set.all()