#
# Helpful Links
# 1. https://stackoverflow.com/questions/1818310/regular-expression-to-remove-a-files-extension
# 2. https://wiki.python.org/moin/HandlingExceptions
# 3. https://docs.python.org/2/library/re.html
# 4. https://github.com/artcom-net/mp3-tagger
#

import os
import re

from mp3_tagger import MP3File
from mp3_tagger.exceptions import MP3OpenFileError


starting_directory = "/Users/bszyman/Desktop/music_archive/media"
artist_directories = os.scandir(starting_directory)

for artist_directory in artist_directories:
	if artist_directory.is_dir():
		print(artist_directory.name)
	
		album_directories = os.scandir(artist_directory.path)
		
		for album_directory in album_directories:
			print("  " + album_directory.name)
			
			if album_directory.is_dir():
				song_list = os.scandir(album_directory.path)
			
				for song in song_list:
					if song.is_file():
						regex = re.search('(\d\d) (.*)\.[^.]+$', song.name)
						if regex:
							song_track = regex.group(1)
							song_title = regex.group(2)
							print("    " + song_track + " " + song_title)
							
							try:
								mp3 = MP3File(song.path)
								mp3.artist = artist_directory.name
								mp3.album = album_directory.name
								mp3.song = song_title
								mp3.track = song_track
								mp3.save()
							except MP3OpenFileError:
								print(" ^ ---- Couldn't open this file.")
