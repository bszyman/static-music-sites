import json
import os
import sys

from models import Album, Collection, Playlist, Track


class MusicLibrary:

    def __init__(self):
        self.base_location = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.media_path = "{0}/media/".format(self.base_location)
        self.playlists = None
        self.collections = None
        self.albums = None
        self.files = None
        self.library_goosed = False

    def goose_up_library(self):
        if not self.files:
            self.files = []

            for (dir_path, dir_name, file_names) in os.walk(self.media_path):
                self.files += [os.path.join(dir_path, file) for file in file_names]

        self.library_goosed = True

    def get_albums(self):
        if not self.library_goosed:
            print("The library is not goosed. Call goose_up_library().")
            return False

        grouped_albums = {}
        idx = 0

        for file in self.files:
            track = Track.init_from_file(file)

            if track:
                album_key = "{0}".format(track.album_title)
                if album_key in grouped_albums:
                    grouped_albums[album_key].tracks.append(track)
                else:
                    new_album = Album(track.album_title, track.artist_name)
                    new_album.tracks.append(track)

                    grouped_albums[album_key] = new_album

                    idx += 1

                    if idx > 6:
                        break

        # collect albums into list
        self.albums = []
        for album_key in grouped_albums.keys():
            album = grouped_albums[album_key]
            album.sort_tracks()

            self.albums.append(album)

        self.albums.sort(key=lambda x: x.title, reverse=False)

        return self.albums

    def get_playlists(self):
        if not self.library_goosed:
            print("The library is not goosed. Call goose_up_library().")
            return False

        if not self.playlists:
            playlists_directory = "{0}/src/playlists".format(self.base_location)
            playlist_files = os.scandir(playlists_directory)
            self.playlists = []

            for playlist_file in playlist_files:
                with open(playlist_file.path) as pfp:
                    playlist_json = json.load(pfp)
                    playlist = Playlist(title=playlist_json["title"])

                    for track_path in playlist_json["tracks"]:
                        track_full_path = "{0}{1}".format(self.media_path, track_path)
                        track = Track.init_from_file(track_full_path)

                        if track:
                            playlist.playlist_tracks.append(track)

                    self.playlists.append(playlist)

        return self.playlists

    def get_collections(self):
        if not self.library_goosed:
            print("The library is not goosed. Call goose_up_library().")
            return False

        if not self.collections:
            collections_directory = "{0}/src/collections".format(self.base_location)
            collection_files = os.scandir(collections_directory)
            self.collections = []

            for collection_file in collection_files:
                with open(collection_file.path) as cfp:
                    collection_json = json.load(cfp)
                    collection = Collection(title=collection_json["title"])

                    for album_path in collection_json["albums"]:
                        album = Album()
                        album_files = os.scandir(album_path)

                        for album_file in album_files:
                            track = Track.init_from_file(album_file.path)

                            if track:
                                album.tracks.append(track)

                                album.title = track.album_title
                                album.artist_name = track.artist_name

                        collection.albums.append(album)
                    self.collections.append(collection)

        return self.collections
