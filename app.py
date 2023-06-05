import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

def descargar_cancion():
    nombre = nombre_cancion.get()
    enlace = enlace_youtube.get()

    try:
        video = YouTube(enlace)
        audio = video.streams.filter(only_audio=True).first()

        # Mostrar el diálogo para seleccionar la carpeta de destino
        directorio_destino = filedialog.askdirectory()

        # Comprobar si se seleccionó una carpeta
        if directorio_destino:
            audio.download(output_path=directorio_destino, filename=nombre + '.mp3')
            messagebox.showinfo("Descarga completada", "La canción se ha descargado correctamente.")
        else:
            messagebox.showwarning("Carpeta no seleccionada", "No se ha seleccionado ninguna carpeta de destino.")
    except Exception as e:
        messagebox.showerror("Error de descarga", str(e))

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Descargar canciones")
ventana.geometry("400x200")

etiqueta1 = tk.Label(ventana, text="Nombre de la canción:")
etiqueta1.pack()

nombre_cancion = tk.Entry(ventana)
nombre_cancion.pack()

etiqueta2 = tk.Label(ventana, text="Enlace de YouTube:")
etiqueta2.pack()

enlace_youtube = tk.Entry(ventana)
enlace_youtube.pack()

boton_descargar = tk.Button(ventana, text="Descargar canción", command=descargar_cancion)
boton_descargar.pack()

ventana.mainloop()

