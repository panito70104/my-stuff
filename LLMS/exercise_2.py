import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

texto = "¡Estamos aprendiendo procesamiento de lenguaje natural con Python!"
# Falta algo acá

tokens = word_tokenize(texto.lower())
stopwords = set(stopwords.words("spanish"))

# Eliminar stopwords
palabras_filtradas = [palabra for palabra in tokens if palabra not in stopwords]

print(palabras_filtradas)
