import tkinter as tk
import youtube_dl

def descargar_cancion():
    enlace = enlace_entry.get()
    opciones = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    try:
        with youtube_dl.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(enlace, download=False)
            titulo = info.get('title', None)
            if titulo:
                ydl.download([enlace])
                resultado_label.config(text="Canción descargada: {}".format(titulo))
            else:
                resultado_label.config(text="No se pudo obtener información de la canción.")
    except Exception as e:
        resultado_label.config(text="Error al descargar la canción: {}".format(str(e)))

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Descargador de canciones")
ventana.geometry("400x200")

enlace_label = tk.Label(ventana, text="Enlace de YouTube:")
enlace_label.pack()

enlace_entry = tk.Entry(ventana, width=40)
enlace_entry.pack()

descargar_button = tk.Button(ventana, text="Descargar", command=descargar_cancion)
descargar_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()
