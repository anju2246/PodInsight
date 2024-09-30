# podcastApi.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils import get_podcast_id_from_link

def get_episodes_from_podcast(podcast_link):
    client_id = '814dad662351483284f9ecb1f9c622ac'
    client_secret = '1e6238a1125f4bfda146f8c944d43146'
    credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=credentials)

    podcast_id = get_podcast_id_from_link(podcast_link)  # Función de utils.py que obtiene el ID
    episodes = sp.show_episodes(podcast_id)

    return episodes['items']

