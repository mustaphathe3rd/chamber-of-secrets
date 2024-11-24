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
NUM = 10
def get_top_items(spotify, term='short_term', limit=NUM):
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
        
        print("Your Top Albums:")
        data = pd.read_csv("top_albums.csv")
        idx = 1
        for _, row in data.iloc[:NUM].iterrows():  # `_` ignores the row index if not needed
            album_name = row['Album_Name']  # Replace with the exact column name
            artist = row['Artist']         # Replace with the exact column name
            print(f"{idx} {album_name} - {artist}")
            idx += 1
    

    except Exception as e:
        print(f"Error fetching top items: {e}")

if __name__ == "__main__":
    print("Fetching your Spotify stats...\n")
    spotify = spotify_auth()
    if spotify:
        get_top_items(spotify)
