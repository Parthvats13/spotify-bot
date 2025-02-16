# spotify-bot

# Spotify Billboard Playlist Bot

This Python script creates a private Spotify playlist with the top 100 Billboard songs from a specified date. It scrapes the Billboard Hot 100 chart for the given date, searches for the songs on Spotify, and adds them to a newly created playlist.

## Features
- Scrapes Billboard's Hot 100 songs for a given date.
- Searches for the songs on Spotify.
- Creates a private Spotify playlist and adds the songs.

## Requirements
- Python 3.x
- BeautifulSoup (`bs4`)
- Requests
- Spotipy (`spotipy`)

## Installation

1. Clone the repository or copy the script.
   ```bash
   git clone https://github.com/your-username/spotify-billboard-bot.git
   cd spotify-billboard-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually install them:
   ```bash
   pip install bs4 requests spotipy
   ```

3. Set up your Spotify Developer Account:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create an application.
   - Get your **Client ID**, **Client Secret**, and set a **Redirect URI**.

4. Update the script with your credentials:
   ```python
   SPOTIPY_CLIENT_ID = "your_client_id"
   SPOTIPY_CLIENT_SECRET = "your_client_secret"
   SPOTIPY_REDIRECT_URI = "your_redirect_uri"
   ```

## Usage

1. Run the script:
   ```bash
   python spotify_billboard_bot.py
   ```

2. Enter a date in `YYYY-MM-DD` format when prompted.

3. The script will:
   - Fetch the top 100 songs from the Billboard chart.
   - Search for them on Spotify.
   - Create a private playlist and add available songs.

4. The created playlist will be available in your Spotify account.

## Notes
- Some songs may not be available on Spotify and will be skipped.
- Make sure your Spotify account has access to modify playlists.

