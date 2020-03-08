import os
import sys

from jinja2 import Environment, PackageLoader, select_autoescape
from pathlib import Path
from music_library import MusicLibrary

MUSIC_LIBRARY = MusicLibrary()
MUSIC_LIBRARY.goose_up_library()

class ViewController:
    base_location = ""
    env = None

    def __init__(self):
        self.base_location = os.path.dirname(os.path.realpath(sys.argv[0]))

        self.env = Environment(
            loader=PackageLoader('generate', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )


#
# Listing View Controllers
class HomeViewController(ViewController):

    def __init__(self):
        super().__init__()

    def render(self):
        t = self.env.get_template('index.html')
        page = t.render()

        return page

    def render_save(self):
        page = self.render()

        page_path = "{0}/index.html".format(self.base_location)
        page_file_handle = open(page_path, "w")
        page_file_handle.write(page)
        page_file_handle.close()


class AlbumListingViewController(ViewController):

    def __init__(self):
        super().__init__()
        self.library = MUSIC_LIBRARY
        self.album_listing = self.library.get_albums()

    def render(self):
        t = self.env.get_template('index-albums.html')
        page = t.render(albums=self.album_listing)

        return page

    def render_save(self):
        page = self.render()

        page_path = "{0}/albums.html".format(self.base_location)
        page_file_handle = open(page_path, "w")
        page_file_handle.write(page)
        page_file_handle.close()


class CollectionListingViewController(ViewController):

    def __init__(self):
        super().__init__()
        self.library = MUSIC_LIBRARY
        self.collections = self.library.get_collections()

    def render(self):
        t = self.env.get_template('index-collections.html')
        page = t.render(collections=self.collections)

        return page

    def render_save(self):
        page = self.render()

        page_path = "{0}/collections.html".format(self.base_location)
        page_file_handle = open(page_path, "w")
        page_file_handle.write(page)
        page_file_handle.close()


class PlaylistListingViewController(ViewController):

    def __init__(self):
        super().__init__()
        self.library = MUSIC_LIBRARY
        self.playlists = self.library.get_playlists()

    def render(self):
        t = self.env.get_template('index-playlists.html')
        page = t.render(playlists=self.playlists)

        return page

    def render_save(self):
        page = self.render()

        page_path = "{0}/playlists.html".format(self.base_location)
        page_file_handle = open(page_path, "w")
        page_file_handle.write(page)
        page_file_handle.close()

#
#


#
# Detail View Controllers
class AlbumDetailViewController(ViewController):

    def __init__(self, album):
        super().__init__()
        self.album = album

    def render(self):
        template = self.env.get_template('albumDetail.html')
        album_page = template.render(album=self.album)

        return album_page

    def render_save(self):
        album_page = self.render()

        Path(self.base_location + "/album-detail").mkdir(parents=True, exist_ok=True)

        file_out_path = "{0}/album-detail/{1}.html".format(self.base_location, self.album.title)
        album_page_out = open(file_out_path, "w+")
        album_page_out.write(album_page)
        album_page_out.close()


class PlaylistDetailViewController(ViewController):

    def __init__(self, playlist):
        super().__init__()
        self.playlist = playlist

    def render(self):
        template = self.env.get_template('playlistDetail.html')
        playlist_page = template.render(playlist=self.playlist)

        return playlist_page

    def render_save(self):
        playlist_page = self.render()

        Path(self.base_location + "/album-detail").mkdir(parents=True, exist_ok=True)

        file_out_path = "{0}/playlists/{1}.html".format(self.base_location, self.playlist.title)
        playlist_page_out = open(file_out_path, "w+")
        playlist_page_out.write(playlist_page)
        playlist_page_out.close()


class CollectionDetailViewController(ViewController):

    def __init__(self, collection):
        super().__init__()
        self.collection = collection

    def render(self):
        template = self.env.get_template('collectionDetail.html')
        collection_page = template.render(collection=self.collection)

        return collection_page

    def render_save(self):
        collection_page = self.render()

        Path(self.base_location + "/collections").mkdir(parents=True, exist_ok=True)

        file_out_path = "{0}/collections/{1}.html".format(self.base_location, self.collection.title)
        collection_page_out = open(file_out_path, "w+")
        collection_page_out.write(collection_page)
        collection_page_out.close()

#
#


#
# Batch View Controllers
class AlbumPagesBatchViewController(ViewController):
    def __init__(self):
        super().__init__()
        self.library = MUSIC_LIBRARY
        self.albums = self.library.get_albums()

    def go(self):
        for album in self.albums:
            view_controller = AlbumDetailViewController(album)
            view_controller.render_save()


class PlaylistPagesBatchViewController(ViewController):
    def __init__(self):
        super().__init__()
        self.library = MUSIC_LIBRARY
        self.playlists = self.library.get_playlists()

    def go(self):
        for playlist in self.playlists:
            view_controller = PlaylistDetailViewController(playlist)
            view_controller.render_save()


class CollectionPagesBatchViewController(ViewController):
    def __init__(self):
        super().__init__()
        self.library = MUSIC_LIBRARY
        self.collections = self.library.get_collections()

    def go(self):
        for collection in self.collections:
            view_controller = PlaylistDetailViewController(collection)
            view_controller.render_save()
#
#
