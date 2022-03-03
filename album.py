def make_album(artist_name, album_title, num_tracks=''):
    """Generate a dictionary with an album's information"""
    if num_tracks != '':
        return {'artist_name': artist_name, 'album_title': album_title,\
                'tracks': num_tracks}
    else:
        return {'artist_name': artist_name, 'album_title': album_title}

halsey = make_album('Halsey', "If I Can't Have Love, I Want Power")
print(halsey)
porter = make_album('Porter Robinson', "Worlds")
print(porter)
sylvan = make_album('Sylvan Esso', "What Now", '10')
print(sylvan)
