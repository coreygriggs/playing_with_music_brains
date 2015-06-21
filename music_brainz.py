import musicbrainzngs as mbz
import os
import sqlite3


def create_table():
    with sqlite3.connect("output.db") as db:
        db.execute("""CREATE TABLE artists (
            id INTEGER PRIMARY KEY,
            artist_name STRING,
            artist_music_brainz_id STRING
        )""")
        db.commit()


class MusicBrainzQueryInterface():

    def __init__(self, app_name, app_version, contact):
        self.auth = mbz.auth(os.environ['MUSIC_BRAINZ_API_USERNAME'], os.environ['MUSIC_BRAINZ_API_PASSWORD'])
        self.user_agent = mbz.set_useragent(app_name, app_version, contact)
        self.db = sqlite3.connect("output.db")

    def search_artist(self, **artist_args):
        search_fields = ["artists", "releases", "recordings"]
        if len(artist_args) > 1:
            return "You may search by %s, %s, or %s" % artist_args
        for arg in artist_args.keys():
            if arg not in search_fields:
                return "Argument not allowed, possible search terms are: %s" % str(search_fields).replace('[', '').replace(']', '')
            else:
                result = getattr(mbz, "search_%s" % arg)(query=artist_args[arg])
                return result

    def first_artist_parser(self, result):
        """
        :param result : a dictionary containing a list of artists from a search query
        :return dict of artist name and musicbrainz id for the first result
        """
        return dict(artist_name=result['artist-list'][0]['name'],
                    artist_music_brainz_id=result['artist-list'][0]['id'])

    def update_artist_db(self, **artist_info):
        with self.db:
            self.db.execute("INSERT INTO artists (artist_name, artist_music_brainz_id) VALUES ('%s', '%s')" %
                            (artist_info['artist_name'], artist_info['artist_music_brainz_id']))
            self.db.commit()
