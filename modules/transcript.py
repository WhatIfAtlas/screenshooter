from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from modules.utils import create_directory
import os

def fetch_transcript(video_id):
    """
    Tries to fetch the English transcript for a given YouTube video.

    Args:
        video_id (str): YouTube video ID (e.g. 'dQw4w9WgXcQ').

    Returns:
        list[dict] or None: List of transcript entries, or None if not available.
    """
    try:
        transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcripts.find_transcript(['en'])
        return transcript.fetch()
    except (TranscriptsDisabled):
        return None

def save_transcript_to_file(transcript, video_id, output_folder):
    """
    Saves a transcript to a plain text file.

    Args:
        transcript (list[dict]): List of subtitle entries with 'start', 'duration', 'text'.
        video_id (str): The video ID (used for naming the file).
        output_folder (str): Folder where the transcript should be saved.
    """
    create_directory(output_folder)
    path = os.path.join(output_folder, f"{video_id}_transcript.txt")
    with open(path, 'w', encoding='utf-8') as file:
        for entry in transcript:
            start = entry.start
            end = entry.start + entry.duration
            text = entry.text
            file.write(f"{start:.2f} - {end:.2f}: {text}\n")
