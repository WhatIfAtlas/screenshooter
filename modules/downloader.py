import subprocess
import os
from moviepy.editor import VideoFileClip
from PIL import Image
from tqdm import tqdm

from modules.utils import create_directory

def download_video(video_url, output_path, filename):
    """
    Downloads a YouTube video using yt-dlp.

    Args:
        video_url (str): Full YouTube link.
        output_path (str): Folder where the file should go.
        filename (str): Desired filename without extension ('.mp4' will be added).
    """
    create_directory(output_path)
    output_template = os.path.join(output_path, f"{filename}.%(ext)s")

    try:
        subprocess.run(
            [
                'yt-dlp',
                '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                '-o', output_template,
                video_url
            ],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"[Error] yt-dlp failed: {e}")

def create_screenshots(video_path, transcript, output_folder, video_id):
    """
    Saves screenshots from the video at every transcript timestamp.

    Args:
        video_path (str): Path to the downloaded video.
        transcript (list): Transcript entries with .start attribute.
        output_folder (str): Where screenshots should be stored.
        video_id (str): Used for naming the image files.
    """
    clip = VideoFileClip(video_path)

    for entry in tqdm(transcript, desc=f"Creating screenshots for {video_id}"):
        time = entry.start  # changed from ['start'] to .start
        frame = clip.get_frame(time)
        img_path = os.path.join(output_folder, f"{video_id}_{int(time)}.png")
        Image.fromarray(frame).save(img_path)

    clip.close()
