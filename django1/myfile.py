from music.models import Album, Song

a = Album.objects.get(pk=5)



Song.objects.get(pk=3).is_favorite