# Corrige los errores
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
texto = "¡Hola mundo! Estoy aprendiendo NLP."

tokens = word_tokenize(texto)

print(tokens)
