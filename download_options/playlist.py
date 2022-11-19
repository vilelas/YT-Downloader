from pytube import Playlist, YouTube
from pytube.cli import on_progress

import os


def download_playlist(PATH):
    URL = input("URL: ")
        
    try:
        playlist = Playlist(URL)

        new_path = os.path.join(PATH, playlist.title)

        if not os.path.exists(new_path):
            os.mkdir(new_path)

        for video in playlist:
            yt = YouTube(video, on_progress_callback=on_progress)
            # getting the file size
            file_size = yt.streams.get_highest_resolution().filesize / (1024 * 1024)
            print(f"Downloading {yt.title} | File size: {file_size:.2f} MB")
            yt.streams.get_highest_resolution().download(output_path=new_path)
    except Exception as e:
        print(f"ERROR: {e}")