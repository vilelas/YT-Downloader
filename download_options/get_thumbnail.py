import requests
from pytube import YouTube

def obter_url():
   return (YouTube(input("Informe a URL: ")).thumbnail_url).replace("sddefault.jpg", "maxresdefault.jpg")

def baixar_arquivo(url, endereco):
    resposta = requests.get(url, stream=True) 
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
                for parte in resposta.iter_content(chunk_size=256): 
                    novo_arquivo.write(parte)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()