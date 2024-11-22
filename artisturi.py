import spotipy,os
from spotipy.oauth2 import SpotifyOAuth


# Spotify API setup
scope = "user-library-read"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        redirect_uri="http://localhost:8888/callback"
    )
)

# Prepare data for the DataFrame
results = sp.current_user_saved_tracks(limit=50)
tracks_data = []
total_idx = 1  # Global index

while results:
    for item in results['items']:
        track = item['track']
        tracks_data.append([total_idx, track['artists'][0]['name'], track['name']])
        total_idx += 1  # Increment index
    results = sp.next(results)  # Fetch next page
for idx,singer, track_name in tracks_data:
    print(idx,singer,track_name)
import pandas as pd
from collections import Counter

#Write the tracks to a CSV file
'''
df = pd.DataFrame(tracks_data,columns=['Index','Artist','Track'])
df.to_csv("all_tracks.csv",index="False") '''

# Load the saved CSV file
data = pd.read_csv("saved_tracks.csv")

# Count occurrences of each artist
artist_counts = Counter(data["Artist"])

# Find the top 5 most common artists with their frequencies
top_20 = artist_counts.most_common(20)

# Output the results
print("Top 20 artists with their frequencies:")
for artist, frequency in top_20:
    print(f"Artist: {artist}, Frequency: {frequency}")


