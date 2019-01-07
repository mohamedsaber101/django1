from django.db import models

class Album(models.Model):
    def __str__(self):
        return self.album_title + ' - ' + self.artist
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=100)


class Song(models.Model):
    def __str__(self):
        return (self.song_title)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)