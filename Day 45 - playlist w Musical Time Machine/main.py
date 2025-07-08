import requests, os, spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
SPOTIFY_UID = os.environ.get("SPOTIFY_UID")
REDIRECT = "https://example.com/callback"

auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT, scope="playlist-modify-public", cache_path="token.txt", username=SPOTIFY_UID, show_dialog=True)
sp = spotipy.Spotify(auth_manager=auth_manager)

SPOTIFY_UID = sp.current_user()['id']

music_date = input("What date of billboard 100 music do you want? (YYYY-MM-DD): ")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0'
}

with requests.get(f"https://www.billboard.com/charts/hot-100/{music_date}/", headers=headers) as req:
    req.encoding = "utf-8"
    data = req.text

soup = BeautifulSoup(data, 'html.parser')

names = soup.select(".o-chart-results-list__item h3")
# artists = soup.select(".o-chart-results-list__item .c-label")

titles = [name.getText().replace("\n", "").replace("\t", "") for name in names]
playlist = sp.user_playlist_create(SPOTIFY_UID, f"Billboard 100 {music_date}")
input = [sp.search(q=f"track: {title} year: {'-'.split(music_date)[0]}", type="track", limit=1) for title in titles]
final = [input['tracks']['items'][0]['uri'] for input in input]


sp.user_playlist_add_tracks(SPOTIFY_UID, playlist['id'], final)

