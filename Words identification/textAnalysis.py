# text_analysis.py
import nltk
from nltk.corpus import stopwords
from collections import Counter
import spacy

# Cargar recursos de nltk
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Cargar modelo de spaCy para análisis de entidades
nlp = spacy.load('en_core_web_sm')

# Función para analizar los títulos de los episodios
def analyze_titles(titles):
    # Tokenización y conteo de palabras
    words = nltk.word_tokenize(" ".join(titles))
    words_filtered = [word for word in words if word.isalpha() and word.lower() not in stop_words]
    word_freq = Counter(words_filtered)
    
    # Imprimir las palabras más comunes
    print("Palabras más comunes en los títulos:")
    print(word_freq.most_common(10))

# Función opcional para analizar temas usando entidades nombradas
def analyze_topics(titles):
    doc = nlp(" ".join(titles))
    print("Entidades reconocidas en los títulos:")
    for ent in doc.ents:
        print(ent.text, ent.label_)
