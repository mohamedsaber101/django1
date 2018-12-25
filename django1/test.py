from music.models import Album,Song
new_album = Album.objects.get(pk=6)
new_album.album_title

new_song = Song()
new_song.album = new_album
new_song.file_type = 'mp3''
new_song.song_title = 'yalinux'
new_song.album
