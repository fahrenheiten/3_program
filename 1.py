import moviepy.editor
from pathlib import Path

video_file = Path('Изучение C++ для начинающих _ #26 – Заключительный урок.mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')