# data_processing.py
import pandas as pd

# Función para procesar datos de episodios
def process_episode_data(episodes):
    titles = [episode['name'] for episode in episodes]
    durations = [episode['duration_ms'] / 60000 for episode in episodes]  # Convertir milisegundos a minutos
    
    # Crear un DataFrame de pandas para organizar los títulos y las duraciones
    df = pd.DataFrame({
        'Title': titles,
        'Duration (min)': durations
    })
    
    return df
