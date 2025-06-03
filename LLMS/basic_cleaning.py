import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')

texto = "Hola, ¿cómo estás? Estoy aprendiendo procesamiento de lenguaje natural con Python."

# Tokenizar (convertir a palabras)
tokens = word_tokenize(texto)

# Eliminar signos de puntuación y stopwords
stop_words = set(stopwords.words("spanish"))
tokens_limpios = [t for t in tokens if t.lower() not in stop_words and t not in string.punctuation]

print("Tokens limpios:", tokens_limpios)
