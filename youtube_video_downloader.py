from pytube import YouTube
import time

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ha ocurrido un error")
    print("La descarga se ha completado con éxito")


link = input("Enter the YouTube video URL: ")
st = time.time()
Download(link)
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')