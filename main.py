from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID="6c6e14ecfc4d4bb993e39fffd4f90e8b"
SPOTIPY_CLIENT_SECRET="1c549e44d82d496185046ad8a47f55be"
SPOTIPY_REDIRECT_URI='https://example.com/'

date = input("Which year do you want to travel to? (YYYY-MM-DD): ")
year = date.split("-")[0]

top_songs_endpoint = f"https://www.billboard.com/charts/hot-100/{date}"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(top_songs_endpoint, headers= header)

top_songs_web = response.text
soup = BeautifulSoup(top_songs_web, "html.parser")

songs_list = soup.select("li ul li h3")
songs_list = [song.text.strip() for song in songs_list]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Parth",
    )
)
user_id = sp.current_user()["id"]

song_uris = []

for song in songs_list:
    track = sp.search(q= f"track: {song} year: {year}", type = "track")
    try:
        uri = track["tracks"]["items"][0]["uri"]
        print(song)
        print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user= user_id, 
                                      name= f"{date} Billboard 100", 
                                      public= False, 
                                      description="Top Tracks from back in the Dayz of Brunel")
play_id = playlist["id"]
sp.playlist_add_items(playlist_id= play_id, items=song_uris)