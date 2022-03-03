def make_album(artist_name, album_title, num_tracks=''):
    """Generate a dictionary with an album's information"""
    if num_tracks != '':
        return {'artist_name': artist_name, 'album_title': album_title,\
                'tracks': num_tracks}
    else:
        return {'artist_name': artist_name, 'album_title': album_title}

flag = True

while flag:
    artist_name = input('Enter the artist name: ')
    if artist_name.lower() == 'quit':
        break
    album_title = input('Enter the album title: ')
    if album_title.lower() == 'quit':
        break
    album = make_album(artist_name, album_title)
    print(album)
