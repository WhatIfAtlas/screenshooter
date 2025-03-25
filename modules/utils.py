import os

def create_directory(path):
    """
    Creates a folder if it doesn't already exist.

    Args:
        path (str): Path to the folder that should be created.
    """
    os.makedirs(path, exist_ok=True)