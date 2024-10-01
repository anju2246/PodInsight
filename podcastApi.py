# podcastApi.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils import get_podcast_id_from_link

def get_episodes_from_podcast(podcast_link):
    client_id = 'id'
    client_secret = 'secret'
    credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=credentials)

    podcast_id = get_podcast_id_from_link(podcast_link)  # Función de utils.py que obtiene el ID
    episodes = sp.show_episodes(podcast_id)

    return episodes['items']

