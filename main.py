import os

from utils.path import PATH

from download_options.video import download_video
from download_options.playlist import download_playlist
from download_options.get_thumbnail import baixar_arquivo, obter_url
from download_options.download_channel import download_all_channel


def options():
    list_options = {
        1 : "Baixar vídeo",
        2 : "Baixar playlist",
        3 : "Baixar thumbnail",
        4 : "Baixar todos os vídeos de um canal",
        0 : "Sair"
    }

    for key, value in list_options.items():
        print(f'{[key]} - {value}')

    return int(input("Informe a opção desejada: "))


def main():

    answer = 1

    while answer != 0:
        answer = options()

        if answer == 1:
            download_video(PATH)
        elif answer == 2:
            download_playlist(PATH)
        elif answer == 3:
            URL = obter_url()
            baixar_arquivo(URL, os.path.join(PATH, "thumbnail.jpg"))
        elif answer == 4:
            download_all_channel(PATH)

main()