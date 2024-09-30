
# Función para extraer el ID del podcast a partir del link
def get_podcast_id_from_link(podcast_link):
    try:
        return podcast_link.split('show/')[1]
    except IndexError:
        raise ValueError(f"Invalid podcast link: {podcast_link}")
