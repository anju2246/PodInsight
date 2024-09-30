from podcastApi import get_episodes_from_podcast
from textAnalysis import analyze_titles
from dataProcessing import process_episode_data

def main():
    # Ingresar el link del podcast
    podcast_link = input("Ingresa el link del podcast: ")
    
    # Obtener los episodios desde la API
    episodes = get_episodes_from_podcast(podcast_link)
    
    # Procesar los datos para organizar títulos y duraciones
    df = process_episode_data(episodes)
    
    # Analizar los títulos para ver temas y patrones
    analyze_titles(df['Title'])
    
    print("Análisis completado con éxito.")

if __name__ == "__main__":
    main()


