from urllib.error import URLError
from pytube import Channel

import os

def download_all_channel(PATH):
    URL = input("Informe a URL do canal: ")

    c = Channel(URL)

    new_path = os.path.join(PATH, c.channel_name)

    if not os.path.exists(new_path):
            os.mkdir(new_path)
    try:
        print(f"downloading all the videos from the channel {c.channel_name}")
        for video in c.videos:
            file_size = video.streams.get_highest_resolution().filesize / (1024 * 1024)
            print(f"Downloading {video.title} | File size: {file_size:.2f} MB")
            video.streams.get_highest_resolution().download(output_path=new_path)
    except Exception as e:
        print(f"ERROR: {e}")
