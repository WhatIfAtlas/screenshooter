import ssl
from urllib.parse import urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor
from modules.transcript import fetch_transcript, save_transcript_to_file
from modules.downloader import download_video, create_screenshots
from modules.utils import create_directory
import os

def extract_video_id(url):
    """
    Extracts the video ID from a full YouTube URL.

    Args:
        url (str): Should look like 'https://www.youtube.com/watch?v=...'

    Returns:
        str or None: The ID if found, otherwise None.
    """
    query = parse_qs(urlparse(url).query)
    return query.get('v', [None])[0]

def process_video(video_url):
    """
    Handles the full pipeline for one video: transcript, download, screenshots.

    Args:
        video_url (str): YouTube link (one line from your input file).

    Returns:
        bool: True if successful, False if anything failed.
    """
    video_id = extract_video_id(video_url.strip())
    if not video_id:
        print(f"[Error] Couldn't extract video ID from: {video_url}")
        return False

    transcript = fetch_transcript(video_id)
    if not transcript:
        print(f"[Info] No transcript found for video: {video_id}")
        return False

    output_folder = os.path.join("data", video_id)
    create_directory(output_folder)

    save_transcript_to_file(transcript, video_id, output_folder)

    video_filename = f"{video_id}"
    download_video(video_url, output_folder, video_filename)

    video_path = os.path.join(output_folder, f"{video_filename}.mp4")
    create_screenshots(video_path, transcript, output_folder, video_id)

    os.remove(video_path)
    return True

def main(file_path):
    """
    Reads a list of YouTube URLs from a text file and processes them all.

    Args:
        file_path (str): Path to the .txt file with one URL per line.
    """
    ssl._create_default_https_context = ssl._create_unverified_context

    with open(file_path, 'r') as f:
        urls = f.readlines()

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_video, urls))

    success = sum(1 for r in results if r)
    print(f"\nDone! {success} of {len(urls)} videos processed successfully.")

if __name__ == "__main__":
    file = input("Path to file with YouTube URLs: ")
    main(file)
