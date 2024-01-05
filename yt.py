from pytube import YouTube
import os 

url = "https://www.youtube.com/watch?v=Yi0wQJHekak&ab_channel=RenatoCariani"

video = YouTube(url)

print(f'Título: {video.title}')
print(f'Duração: {video.length} segundos')
print(f'Tamanho do video {video.streams.get_highest_resolution().filesize / (1024 ** 2):.2f} MB')

desktop_path = os.path.expanduser("C:/Users/pedro/Videos")

video.streams.get_highest_resolution().download(output_path=desktop_path)

print('Download finalizado. Video salvo no seu computador')