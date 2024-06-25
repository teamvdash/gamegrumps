import json
import os
import yt_dlp

# Define paths to the to-do and complete folders
todo_path = 'to-do/gamegrumps-todo.json'
complete_path = 'complete/gamegrumps-done.json'

# Function to load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to save JSON data to a file
def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Load secrets from the secrets file
def load_secrets(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

secrets = load_secrets('secrets.json')

# Load configurations
todo_configs = load_json(todo_path)
completed_configs = load_json(complete_path)

# Process the next configuration
if todo_configs:
    config = todo_configs.pop(0)
    downloads = config['downloads']
    links = config['links']

    season = downloads.split(' ')[1]
    path = secrets['path']  # Use the path from the secrets file

    # yt_dlp options with the path from the secrets file
    ydl_opts = {
        'ignoreerrors': True,
        'verbose': True,
        'windowsfilenames': True,
        'paths': {
            'home': f'{path}/{downloads}'
        },
        'outtmpl': f"{path}/{downloads}/Game Grumps - S{season}E%(playlist_index)s - %(title)s.%(ext)s",
        'format': "best",
        'merge_output_format': "mp4",
        "subtitleslangs": ["en"],
        'writesubtitles': True,
        'writeautomaticsub': True,
        "yes-playlist": True
    }

    # Download the videos
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([links])

    # Add the processed configuration to the top of the completed list
    completed_configs.insert(0, config)

    # Save the updated lists
    save_json(todo_path, todo_configs)
    save_json(complete_path, completed_configs)

else:
    print("No configurations to process.")