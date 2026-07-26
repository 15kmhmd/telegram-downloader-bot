import yt_dlp
import os
import uuid

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_video(url: str):
    filename = os.path.join(DOWNLOAD_DIR, str(uuid.uuid4()))

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": filename + ".%(ext)s",
        "noplaylist": True,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        path = ydl.prepare_filename(info)

        if not path.endswith(".mp4"):
            base = os.path.splitext(path)[0]
            if os.path.exists(base + ".mp4"):
                path = base + ".mp4"

        return path
