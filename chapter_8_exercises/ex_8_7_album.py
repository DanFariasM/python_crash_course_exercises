def make_album(artist, album, song_no=None):
    """Describe a music album"""
    artist_album = {"artist": artist, "album": album}
    if song_no:
        artist_album["song_no"] = song_no
    return artist_album

album_info = make_album("haken", "virus")
print(album_info)

album_info = make_album("dream theater", "awake")
print(album_info)

album_info = make_album("symphony x", "the odyssey")
print(album_info)

album_info = make_album("dream theater", "six degrees", 12)
print(album_info)