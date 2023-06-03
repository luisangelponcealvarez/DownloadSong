import tkinter as tk
from pytube import YouTube


def download_video():
    video_url = url_entry.get()
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download()


def download_audio():
    video_url = url_entry.get()
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()


# Crear la ventana principal
window = tk.Tk()
window.title("Descargador de YouTube")

# Crear la etiqueta y la entrada de URL
url_label = tk.Label(window, text="Ingrese la URL del video de YouTube:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Crear los botones de descarga de video y audio
video_button = tk.Button(window, text="Descargar video", command=download_video)
video_button.pack()
audio_button = tk.Button(window, text="Descargar audio", command=download_audio)
audio_button.pack()

# Iniciar el bucle principal de la ventana
window.mainloop()
