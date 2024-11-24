import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Scopes define what data you want to access
SCOPE = 'user-top-read'

def spotify_auth():
    """Authenticate with Spotify API using client credentials."""
    try:
        auth_manager = SpotifyOAuth(
            client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
            client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
            redirect_uri='http://localhost:8888/callback',
            scope=SCOPE
        )
        return spotipy.Spotify(auth_manager=auth_manager)
    except Exception as e:
        print(f"Error during authentication: {e}")
        return None
NUM = 50
def get_top_items(spotify, term='medium_term', limit=NUM):
    """
    Fetch top artists or tracks based on time range.
    term options: 'short_term' (4 weeks), 'medium_term' (6 months), 'long_term' (years)
    """
    try:
        top_tracks = spotify.current_user_top_tracks(time_range=term, limit=limit)
        top_artists = spotify.current_user_top_artists(time_range=term, limit=limit)
        

        print("Your Top Tracks:")
        for i, track in enumerate(top_tracks['items'], 1):
            print(f"{i}. {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")

        print("\nYour Top Artists:")
        for i, artist in enumerate(top_artists['items'], 1):
            print(f"{i}. {artist['name']}")
        
        albums = {}

        # Extract album details from tracks
        for item in top_tracks['items']:
            album = item['album']
            album_name = album['name']
            artist_name = album['artists'][0]['name']
            album_id = album['id']

            # Avoid duplicates
            if album_id not in albums:
                albums[album_id] = {
                    "Album Name": album_name,
                    "Artist": artist_name,
                }

        # Print or Save Top Albums

        print("\nTop Albums:")
        idx = 1
        for album_id, details in albums.items():
            print(f"{idx}. {details['Album Name']} by {details['Artist']}")
            idx+=1

    except Exception as e:
        print(f"Error fetching top items: {e}")

if __name__ == "__main__":
    print("Fetching your Spotify stats...\n")
    spotify = spotify_auth()
    if spotify:
        get_top_items(spotify)
