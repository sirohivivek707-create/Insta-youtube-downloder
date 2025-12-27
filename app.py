from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        ydl_opts = {
            'outtmpl': 'download.%(ext)s',
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir():
            if file.startswith("download"):
                return send_file(file, as_attachment=True)
    return render_template('index.html')

app.run(host='0.0.0.0', port=10000)
