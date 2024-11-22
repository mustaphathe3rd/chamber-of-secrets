import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from requests.exceptions import HTTPError

# Retrieve environment variables
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")

# Ensure credentials are available
if not SPOTIPY_CLIENT_ID or not SPOTIPY_CLIENT_SECRET:
    print("Error: Spotify credentials are not set in environment variables.")
    exit()

# Authenticate with Spotify
try:
    client_credentials_manager = SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
    )
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Search for the artist
    artist_name = input("Artist: ")
    results = spotify.search(q=artist_name, type='artist', limit=3)
    
    # Check if results are empty
    if not results['artists']['items']:
        print(f"No artist found for the name: {artist_name}")
        exit()
    
    
    # Extract and print artist information
    artist = results['artists']['items'][0]
    print(f"Artist Name: {artist['name']}")
    artist_uri = artist['uri']
    results = spotify.artist_albums(artist_uri,album_type='album')
    albums = results['items']

    # Paginate through the results
    if results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
    print("List of ALbums:")

# Print album names
    for album in albums:
        print(album['name'])
        
    print(f"No of albums: {len(albums)}")
except HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    

