import musicbrainzngs as mbz
import os

def authorize():
    mbz.auth(os.environ['MUSIC_BRAINS_API_USERNAME'], os.environ['MUSIC_BRAINS_API_PASSWORD'])

def search_artist(**artist_args):
    search_fields = ["gender", "artist", "type"]
    for arg in artist_args.keys():
        if arg not in search_fields:
            return "Argument not allowed, required search terms are: %s" % str(search_fields).replace('[', '').replace(']', '')