import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def download_video():
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4", initialfile=yt.title)
        if file_path:
            video.download(output_path=file_path)
            status_label.config(text="Descarga completada")
        else:
            status_label.config(text="Descarga cancelada")
    except Exception as e:
        status_label.config(text=str(e))

def download_audio():
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        audio = yt.streams.filter(only_audio=True).first()
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", initialfile=yt.title)
        if file_path:
            audio.download(output_path=file_path)
            status_label.config(text="Descarga completada")
        else:
            status_label.config(text="Descarga cancelada")
    except Exception as e:
        status_label.config(text=str(e))

# Crear la ventana principal
window = tk.Tk()
window.title("Descargador de YouTube")

# Crear los elementos de la interfaz
url_label = tk.Label(window, text="URL del video:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

video_button = tk.Button(window, text="Descargar Video", command=download_video)
video_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E+tk.W)

audio_button = tk.Button(window, text="Descargar Audio", command=download_audio)
audio_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E+tk.W)

status_label = tk.Label(window, text="")
status_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Configurar el espaciado entre las columnas
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Iniciar el bucle de eventos
window.mainloop()
