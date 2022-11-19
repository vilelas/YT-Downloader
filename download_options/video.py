from pytube import YouTube
from pytube.cli import on_progress


def download_video(PATH):
    URL = input("URL: ")

    try:
        yt = YouTube(URL, on_progress_callback=on_progress)
        # getting the file size
        file_size = yt.streams.get_highest_resolution().filesize / (1024 * 1024)
        print(f"Downloading {yt.title} | File size: {file_size:.2f} MB")
        yt.streams.get_highest_resolution().download(output_path=PATH)
    except Exception as e:
        print(f"ERROR: {e}")