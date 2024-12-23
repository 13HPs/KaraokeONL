import io
import sys
import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
from pydub import AudioSegment

load_dotenv('D:\PBL6\.env')

cloudinary.config(
    cloud_name='dddiwftri',  # Replace with your Cloudinary cloud name
    api_key='171257253152235',  # Replace with your Cloudinary API key
    api_secret='vs9TyZ8sQs4lMYP4Sqt0p1_O9Sg'  # Replace with your Cloudinary API secret
)
# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import re
from mongoengine import connect
from app.models.music import Music
from app.models.genre import Genre
from app.models.artist import Artist

connect('PBL6')
def parse_lyrics(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lyrics_data = []
    order = 1
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Skip empty lines
        if not line:
            i += 1
            continue

        # Parse timestamp line
        match = re.match(r"(\d{2}:\d{2}:\d{2}\.\d{3})\s-->\s(\d{2}:\d{2}:\d{2}\.\d{3})", line)
        if match:
            start_time, end_time = match.groups()

            # Move to next line for lyrics
            i += 1
            if i < len(lines):
                lyric_line = lines[i].strip()

                # Only add if we have both timestamp and lyrics
                lyrics_data.append({
                    "order": order,
                    "start_time": start_time,
                    "end_time": end_time,
                    "text": lyric_line,
                    "artist_index": 0
                })
                order += 1
        i += 1

    return lyrics_data
# Base directory: the directory where the current script is located
base_dir = os.path.dirname(__file__)  # This will give the directory of save_music.py

# Correct file path
file_path = os.path.join(base_dir, 'datasets', 'son_tung', 'chung_ta_khong_thuoc_ve_nhau', 'lyrics.vtt')

lyrics_data = parse_lyrics(file_path)
print(lyrics_data)
# exit(1)
lyrics = [lyric['text'] for lyric in lyrics_data]
music_path = r'D:\PBL6\test\datasets\son_tung\chung_ta_khong_thuoc_ve_nhau\no_vocals.wav'
with open(music_path, 'rb') as file:
    buffer = io.BytesIO(file.read())
public_id = "chung_ta_khong_thuoc_ve_nhau_audio"
if not os.path.exists(music_path):
    print(f"File not found: {music_path}")
    exit(1)
try:
    response = cloudinary.uploader.upload(
        buffer,
        resource_type="auto",
        public_id="son_tung/chung_ta_khong_thuoc_ve_nhau",
        folder="music"
    )
    print("Upload Response:", response)  # Debugging
    music_url = response['secure_url']
except Exception as e:
    print(f"Error type: {type(e)}")
    print(f"Error message: {str(e)}")
    exit(1)
Music(music_url=music_url, name='Chúng ta không thuộc về nhau', lyrics=lyrics_data, artists=[Artist.objects(username='Sơn Tùng M-TP').first()], genres=[Genre.objects(name="pop").first()]).create()
