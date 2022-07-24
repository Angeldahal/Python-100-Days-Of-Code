import requests

CLIENT_ID = "02036b1520b74df690ae05c983dd2b8b"
AUTH_TOKEN = "710ae206030846a1a0d3d0b5abe07601"

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=AUTH_TOKEN,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]