from __future__ import unicode_literals
import yt_dlp as youtube_dl
import os
import time
import os
import shutil
from pydub import AudioSegment
import random
import string

MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB
MAX_TOTAL_SIZE = 100 * 1024 * 1024  # 100 MB

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

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def my_hook(d):
    print("hook", d["status"])
    if d["status"] == "finished":
        print("Done downloading, now converting ...")


def get_ydl_opts(external_logger=lambda x: None, suffix=""):
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
        "outtmpl": f"./downloads/audio/%(title)s_{suffix}.%(ext)s",  # Set the output filename directly
        "progress_hooks": [my_hook],
    }

def segment_audio(file_path, max_size=MAX_FILE_SIZE):
    audio = AudioSegment.from_file(file_path)
    duration_ms = len(audio)
    
    # Calculate segment duration based on file size and audio properties
    bytes_per_ms = (audio.frame_rate * audio.sample_width * audio.channels) / 1000

    # Adjust for MP3 compression with margin for error
    estimated_compression_ratio = 0.2
    adjusted_bytes_per_ms = bytes_per_ms * estimated_compression_ratio

    segment_duration_ms = int(max_size / adjusted_bytes_per_ms)
    
    segments = []
    for start_ms in range(0, duration_ms, segment_duration_ms):
        end_ms = min(start_ms + segment_duration_ms, duration_ms)
        segment = audio[start_ms:end_ms]
        
        segment_file_path = f"{os.path.splitext(file_path)[0]}_segment_{start_ms // segment_duration_ms}.mp3"
        print(f"Saving segment {segment_file_path}...")
        segment.export(segment_file_path, format="mp3", bitrate="192k")
        
        # Check if the exported file is within the size limit
        if os.path.getsize(segment_file_path) > max_size:
            os.remove(segment_file_path)
            raise ValueError(f"Segment {start_ms // segment_duration_ms} exceeds the maximum file size after export.") # TODO: Add alternative approach that tries to create a smaller segment on this ValueError
        
        segments.append(segment_file_path)
    
    return segments

def get_file_size(file_path):
    return os.path.getsize(file_path)


def download_video_audio(url, external_logger=lambda x: None):
    retries = 0
    while retries < max_retries:
        try:
            suffix = random_string()
            ydl_opts = get_ydl_opts(external_logger, suffix=suffix)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Going to download ", url)
                info = ydl.extract_info(url, download=False)
                filename = ydl.prepare_filename(info)
                res = ydl.download([url])
                print("youtube-dl result :", res)
                mp3_filename = os.path.splitext(filename)[0] + '.mp3'
                print('mp3 file name - ', mp3_filename)
                
                file_size = get_file_size(mp3_filename)

                if file_size < MAX_FILE_SIZE:
                    # No segmenting needed, file <25 MB
                    return [mp3_filename]
                elif file_size <= MAX_TOTAL_SIZE:
                    # If below upper limit, segment audio into several <25 MB files
                    return segment_audio(mp3_filename)
                else:
                    # Raise error as file exceeds upper bound
                    raise ValueError(f"File size exceeds {(MAX_TOTAL_SIZE/(1024 * 1024))} MB limit")

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