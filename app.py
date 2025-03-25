from flask import Flask, request, render_template
import yt_dlp

app = Flask(__name__)

def download_video(url):
    ydl_opts = {'outtmpl': 'downloads/%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["url"]
        download_video(video_url)
        return "Download Started!"
    return '''
        <form method="post">
            <input type="text" name="url" placeholder="Enter Video URL">
            <button type="submit">Download</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
