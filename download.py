from __future__ import unicode_literals
import yt_dlp as youtube_dl
import os
import time

max_retries = 3
delay = 2


class MyLogger(object):
    def __init__(self, external_logger=lambda x: None):
        self.external_logger = external_logger

    def debug(self, msg):
        print("[debug]: ", msg)
        self.external_logger(msg)

    def warning(self, msg):
        print("[warning]: ", msg)

    def error(self, msg):
        print("[error]: ", msg)


def my_hook(d):
    print("hook", d["status"])
    if d["status"] == "finished":
        print("Done downloading, now converting ...")


def get_ydl_opts(external_logger=lambda x: None):
    return {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
                "preferredquality": "192",  # set the preferred bitrate to 192kbps
            }
        ],
        "logger": MyLogger(external_logger),
    "outtmpl": "./downloads/audio/%(title)s.%(ext)s",  # Set the output filename directly
    "progress_hooks": [my_hook],
}


def download_video_audio(url, external_logger=lambda x: None):
    retries = 0
    while retries < max_retries:
        try:
            ydl_opts = get_ydl_opts(external_logger)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Going to download ", url)
                info = ydl.extract_info(url, download=False)
                filename = ydl.prepare_filename(info)
                res = ydl.download([url])
                print("youtube-dl result :", res)
                mp3_filename = os.path.splitext(filename)[0] + '.mp3'
                print('mp3 file name - ', mp3_filename)
                return mp3_filename
        except Exception as e:
            retries += 1
            print(
                f"An error occurred during downloading (Attempt {retries}/{max_retries}):",
                str(e),
            )
            if retries >= max_retries:
                raise e
            time.sleep(delay)
