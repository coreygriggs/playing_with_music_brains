import musicbrainzngs as mbz
import os

def authorize(app_name, app_version, contact):
    mbz.auth(os.environ['MUSIC_BRAINZ_API_USERNAME'], os.environ['MUSIC_BRAINZ_API_PASSWORD'])
    mbz.set_useragent(app_name, app_version, contact)

def search_artist(**artist_args):
    search_fields = ["artist", "release", "recording"]
    
    if len(artist_args) > 1:
  		return "You may search by %s, %s, or %s" % artist_args
    for arg in artist_args.keys():
        if arg not in search_fields:
            return "Argument not allowed, possible search terms are: %s" % str(search_fields).replace('[', '').replace(']', '')
    
    if "artist" in artist_args.keys():
    	results = mbz.search_artists(artist)
    if "release" in artist_args.keys():
    	results = mbz.search_releases(release)
   	if "recording" in artist_args.keys():
   		results = mbs.search_recordings(recording)
    return results