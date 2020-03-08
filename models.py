from mp3_tagger import MP3File
from mp3_tagger.exceptions import MP3OpenFileError


class Track:
    def __init__(self, file_path="", album_title="", title="", artist_name="", time="", track_no=0):
        self.file_path = file_path
        self.album_title = album_title
        self.title = title
        self.artist_name = artist_name
        self.time = time
        self.track_no = track_no

    @staticmethod
    def init_from_file(audio_file_path):
        try:
            mp3 = MP3File(audio_file_path)
            tags = mp3.get_tags()
            album_title = tags["ID3TagV2"]["album"]
            title = tags["ID3TagV2"]["song"]
            artist_name = tags["ID3TagV2"]["artist"]
            track_no = int(tags["ID3TagV2"]["track"])

            track = Track(
                audio_file_path,
                album_title,
                title,
                artist_name,
                "0:00",
                track_no
            )

            return track
        except MP3OpenFileError:
            print(audio_file_path)
            print(" ^ ---- Couldn't open this file.")

            return False


class Album:
    def __init__(self, title="", artist_name=""):
        self.title = title
        self.artist_name = artist_name
        self.tracks = []

    def sort_tracks(self):
        self.tracks.sort(key=lambda x: x.track_no, reverse=False)


class Playlist:
    def __init__(self, title="", playlist_tracks=[]):
        self.title = title
        self.playlist_tracks = playlist_tracks


class Collection:
    def __init__(self, title="", albums=[]):
        self.title = title
        self.albums = albums
