from __future__ import unicode_literals
import yt_dlp as youtube_dl
import os
import time
import os
import shutil

MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB
FILE_TOO_LARGE_MESSAGE = "The audio file is too large for the current size and rate limits using Whisper. If you used a YouTube link, please try a shorter video clip. If you uploaded an audio file, try trimming or compressing the audio to under 25 MB."
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
                filesize = info.get("filesize", 0)
                if filesize > MAX_FILE_SIZE:
                    raise Exception(FILE_TOO_LARGE_MESSAGE)
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



def delete_download(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"File {path} has been deleted.")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Directory {path} and its contents have been deleted.")
        else:
            print(f"The path {path} is neither a file nor a directory.")
    except PermissionError:
        print(f"Permission denied: Unable to delete {path}.")
    except FileNotFoundError:
        print(f"File or directory not found: {path}")
    except Exception as e:
        print(f"An error occurred while trying to delete {path}: {str(e)}")
        