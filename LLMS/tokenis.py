from docx import Document
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

# Abre el archivo DOCX
doc = Document("H.docx")

# Extrae el texto
texto = "\n".join([p.text for p in doc.paragraphs])

# Tokeniza
tokens = word_tokenize(texto)
print(tokens)

    