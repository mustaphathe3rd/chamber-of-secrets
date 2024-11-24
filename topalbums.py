import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pandas as pd

'''# Spotify API setup
scope = "user-top-read"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        redirect_uri="http://localhost:8888/callback"
    )
)

# Parameters
time_range = "medium_term"  # Options: 'short_term', 'medium_term', 'long_term'
limit = 50  # Max limit is 50

# Fetch top tracks
top_tracks = sp.current_user_top_tracks(time_range=time_range, limit=limit)
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

print("Top Albums:")
for album_id, details in albums.items():
    print(f"{details['Album Name']} by {details['Artist']}")
   
# Convert albums dictionary to a DataFrame
top_albums_df = pd.DataFrame.from_dict(albums, orient='index')  # Extract values as rows

# Save DataFrame to a CSV file
top_albums_df.to_csv("top_albums.csv", index=False)

print("Top albums saved to top_albums.csv")'''

# Load the CSV file
data = pd.read_csv("top_albums.csv")

# Iterate over rows in the DataFrame
idx = 1
for _, row in data.iloc[:50].iterrows():  # `_` ignores the row index if not needed
    album_name = row['Album_Name']  # Replace with the exact column name
    artist = row['Artist']         # Replace with the exact column name
    print(f"{idx} {album_name} - {artist}")
    idx += 1
    