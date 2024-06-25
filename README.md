# GAME GRUMPS

## Overview
This project automates the process of downloading and organizing Game Grumps videos from YouTube using `yt_dlp`. It uses configuration files to manage download tasks and a secrets file to store sensitive information like the download path.

## Directories
The project requires a `secrets.json` file to specify the download path. The structure of the directories and the path setup is essential for organizing the downloaded videos properly.

### Secrets File
Create a `secrets.json` file in the root directory of your project. This file contains the base path where the videos will be downloaded. Make sure to set the path according to your system setup. Here’s an example of what the file should look like:

```json
{
    "path": "/youtube-videos/Game Grumps"
}
```

### Final Path Structure

Using the stock code, the final path for the downloaded videos will look like:

```
/youtube-videos/Game Grumps/Season 426 - Amanda The Adventurer/Game Grumps - S426E1 - Wholesome + Cute Games Only ｜ Amanda the Adventurer
```

## Requirements

```
pip install yt-dlp
# For macOS
brew install ffmpeg
# For Ubuntu/Debian
sudo apt-get install ffmpeg
```

## Add to the to-do file

```json
[
    {
        "downloads": "Season 426 - Amanda The Adventurer",
        "links": "https://www.youtube.com/watch?v=-Xp-xvlbsQ0&list=PLRQGRBgN_EnpFJGT4_5QFTLsyfB7Fksu9"
    },
    {
        "downloads": "Season 427 - Another Series",
        "links": "https://www.youtube.com/watch?v=another_link"
    }
]
```

## Run script

```python
python yt-dlp.py
```

## Process

The script will downlaod a playlist of videos and use the path in secrets.json to store the files. It will then take the todo entries and put them in completed one done.

# Contributing

If you have any suggestions or improvements, feel free to submit a pull request or open an issue.

# License
This project is licensed under the MIT License.

This `README.md` provides a clear and detailed explanation of the project's setup, requirements, configuration, and usage, making it easier for others to understand and use your project. The script ensures new entries are added to the top of the completed JSON file, preserving the history of completed downloads.