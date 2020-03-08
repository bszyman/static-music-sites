from controllers import (
    AlbumListingViewController,
    AlbumPagesBatchViewController,
    CollectionListingViewController,
    CollectionPagesBatchViewController,
    HomeViewController,
    PlaylistListingViewController,
    PlaylistPagesBatchViewController
)


if __name__ == "__main__":
    # homepage
    home_vc = HomeViewController()
    home_vc.render_save()

    # albums index
    album_index_vc = AlbumListingViewController()
    album_index_vc.render_save()

    # collections index
    collection_index_vc = CollectionListingViewController()
    collection_index_vc.render_save()

    # playlists index
    playlist_index_vc = PlaylistListingViewController()
    playlist_index_vc.render_save()

    # generate album pages
    AlbumPagesBatchViewController().go()

    # generate playlist pages
    PlaylistPagesBatchViewController().go()

    # generate collection pages
    CollectionPagesBatchViewController().go()
