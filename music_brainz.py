import musicbrainzngs as mbz
import os

def authorize(app_name, app_version, contact):
    mbz.auth(os.environ['MUSIC_BRAINZ_API_USERNAME'], os.environ['MUSIC_BRAINZ_API_PASSWORD'])
    mbz.set_useragent(app_name, app_version, contact)

def search_artist(**artist_args):
    search_fields = ["gender", "artist", "type"]
    for arg in artist_args.keys():
        if arg not in search_fields:
            return "Argument not allowed, required search terms are: %s" % str(search_fields).replace('[', '').replace(']', '')
    return mbz.search_artists(gender=artist_args['gender'])