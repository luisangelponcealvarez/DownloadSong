from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            video = YouTube(url)
            audio_stream = video.streams.filter(only_audio=True).first()
            audio_stream.download()
            message = "El audio se ha descargado correctamente."
        except Exception as e:
            message = f"Error: {str(e)}"
        return render_template('index.html', message=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
