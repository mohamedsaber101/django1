from music.models import  Album

a=Album()
a.album_title = "first titleeee"
a.save()
print (a.album_title)