def make_album(artist, album):
    """Describe a music album"""
    artist_album = {"artist": artist, "album": album}
    return artist_album

while True:
    print("\nPlease tell me some information about your favorite album:")
    print("Enter 'q' to quit at any point")
    artist_name = input("What is the artist name: ")
    if artist_name == 'q':
        break
    album_name = input("What is the album name: ")
    if album_name == 'q':
        break

    album_info = make_album(artist_name, album_name)
    print(album_info)