from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import pandas as pd

# Load the main video file
video = VideoFileClip("memento.mkv")

# Define the start and end times for clips to reverse
start_time, start_time2 = 20, 119
end_time, end_time2 = 119, 154

# Extract and reverse the specified clips
clip_to_reverse = video.subclip(start_time, end_time).fx(vfx.time_mirror)
clip_to_reverse2 = video.subclip(start_time2, end_time2).fx(vfx.time_mirror)

# Read the CSV file containing scene start and end times
data = pd.read_csv("scenes.csv")

# Create a list of clips in chronological order
chronological_scenes = [ 
    video.subclip(row["start"], row["end"]) for _, row in data.iterrows()
]

# Combine chronological scenes with the reversed clips
all_clips = chronological_scenes + [clip_to_reverse2, clip_to_reverse]

# Concatenate all clips into a single video
memento_new = concatenate_videoclips(all_clips)

# Write the output to a new video file
memento_new.write_videofile("memento_chronological.mp4", codec="libx264")
