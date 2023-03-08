from art import *
import moviepy.editor
from pathlib import Path

tprint('jalieren')

print('Your video should be in the same directory as a script')
try:
    vid_name = str(input('Your video name: '))
    video_file = Path(f'{vid_name}.mp4')
    video = moviepy.editor.VideoFileClip(f'{video_file}')
    audio = video.audio
    audio.write_audiofile(f'{video_file.stem}.mp3')
except OSError:
    print("File not found")
    exit()
