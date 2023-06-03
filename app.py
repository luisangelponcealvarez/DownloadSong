import tkinter as tk
from pytube import YouTube
import pygame

def descargar_cancion():
    url = entry.get()
    carpeta_destino = entry_carpeta.get()

    try:
        video = YouTube(url)
        cancion = video.streams.filter(only_audio=True).first()
        archivo_destino = cancion.download(output_path=carpeta_destino)
        status_label.config(text="¡Descarga completa!")
        reproducir_cancion(archivo_destino)
    except Exception as e:
        status_label.config(text="Error al descargar la canción: " + str(e))

def reproducir_cancion(archivo):
    pygame.mixer.init()
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Descargador y reproductor de canciones")

# Etiqueta y campo de entrada para la URL
label_url = tk.Label(ventana, text="URL de YouTube:")
label_url.pack()
entry = tk.Entry(ventana)
entry.pack()

# Etiqueta y campo de entrada para la carpeta de destino
label_carpeta = tk.Label(ventana, text="Carpeta de destino:")
label_carpeta.pack()
entry_carpeta = tk.Entry(ventana)
entry_carpeta.pack()

# Botón de descarga
boton_descargar = tk.Button(ventana, text="Descargar y Reproducir", command=descargar_cancion)
boton_descargar.pack()

# Etiqueta de estado
status_label = tk.Label(ventana, text="")
status_label.pack()

# Ejecutar la ventana
ventana.mainloop()
