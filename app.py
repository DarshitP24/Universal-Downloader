from flask import Flask, render_template, request, send_file, after_this_request, jsonify
import yt_dlp
import os, re, tempfile

app = Flask(__name__)
progress_data = {"percent": 0}


def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)


def progress_hook(d):
    if d['status'] == 'downloading':
        p = d.get('_percent_str', '0.0%').replace('%', '').strip()
        try:
            progress_data["percent"] = int(float(p))
        except:
            pass
    elif d['status'] == 'finished':
        progress_data["percent"] = 100


@app.route("/progress")
def progress():
    return jsonify(progress_data)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        quality = request.form.get("quality", "720")
        mode = request.form.get("mode", "video")
        progress_data["percent"] = 0

        try:
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                title = sanitize_filename(info.get('title', 'media'))

            temp_dir = tempfile.mkdtemp()

            base_opts = {
                "progress_hooks": [progress_hook],
                "quiet": True,
                "noplaylist": True,
                "merge_output_format": "mp4",
                # For private sites if needed:
                # "cookiesfrombrowser": ("chrome",),
            }

            if mode == "audio":
                filename = f"{title}.mp3"
                filepath = os.path.join(temp_dir, filename)

                ydl_opts = {
                    **base_opts,
                    "format": "bestaudio/best",
                    "outtmpl": os.path.join(temp_dir, f"{title}.%(ext)s"),
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }],
                }
            else:
                filename = f"{title}.mp4"
                filepath = os.path.join(temp_dir, filename)

                # ✅ FIX: force MP4 video + M4A(AAC) audio → no Opus → audio works everywhere
                ydl_opts = {
                    **base_opts,
                    "format": f"bestvideo[ext=mp4][height<={quality}]+bestaudio[ext=m4a]/best[ext=mp4]",
                    "outtmpl": filepath,
                    "merge_output_format": "mp4",
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            @after_this_request
            def cleanup(response):
                try:
                    for f in os.listdir(temp_dir):
                        os.remove(os.path.join(temp_dir, f))
                    os.rmdir(temp_dir)
                except:
                    pass
                return response

            return send_file(filepath, as_attachment=True, download_name=filename)

        except Exception as e:
            msg = str(e)

            if "Unsupported URL" in msg:
                msg = "Unsupported or invalid link."
            elif "404" in msg or "not found" in msg.lower():
                msg = "Video not found. It may be removed."
            elif "Private video" in msg:
                msg = "This video is private."
            elif "Sign in" in msg or "login" in msg.lower():
                msg = "Login required to access this video."
            else:
                msg = "Failed to fetch video. Please try another link."

            return jsonify({"error": msg}), 400

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
