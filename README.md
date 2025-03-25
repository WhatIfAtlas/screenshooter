
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
```

## 🚀 Usage

Create a text file with YouTube URLs (one per line), e.g.:

```
video_urls.txt
```

Then run:

```bash
python main.py
```

You'll be asked for the input file name (e.g. `video_urls.txt`), and the tool will:

- Download the video using `yt-dlp`
- Fetch the English transcript (if available)
- Generate screenshots at each subtitle timestamp
- Save everything in a structured folder like this:

```
data/
└── dQw4w9WgXcQ/
    ├── dQw4w9WgXcQ_transcript.txt
    ├── dQw4w9WgXcQ_5.png
    ├── dQw4w9WgXcQ_12.png
    └── ...
```

Each screenshot corresponds to a caption timestamp — ideal for generating aligned image/text training data.

## 🙋‍♂️ Why?

Originally developed for a pathology AI project — but applicable to anything involving aligned image/text data from YouTube.

## 🛠️ Built With

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [moviepy](https://github.com/Zulko/moviepy)
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
- [Pillow](https://python-pillow.org/)
- [tqdm](https://github.com/tqdm/tqdm)

---

> Created with love, focus and some late-night coding sessions ☕💻  
> by [WhatIfAtlas](https://github.com/WhatIfAtlas)
