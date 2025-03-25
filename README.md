# Screenshooter 🎥📸

Extracts transcripts and screenshots from YouTube videos — useful for building datasets (e.g. for pathology-related AI models).

## 🔧 Features

- Downloads any public YouTube video
- Fetches English transcript automatically
- Generates frame-accurate screenshots at each caption timestamp
- Structured output folders
- Simple command line usage
- Built with `yt-dlp`, `moviepy`, and `youtube-transcript-api`

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/WhatIfAtlas/screenshooter.git
cd screenshooter
pip install -r requirements.txt
