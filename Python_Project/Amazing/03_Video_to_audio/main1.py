import moviepy.editor as mp
clip = mp.VideoFileClip(r"DhamakaDhoni.mp4")
clip.audio.write_audiofile(r"dhoni2.mp3")