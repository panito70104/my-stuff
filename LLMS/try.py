import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import nltk
import re

nltk.download('punkt')
nltk.download('stopwords')

# Dataset de ejemplo
data = pd.DataFrame({
    'texto': [
        'Me encantó el producto, excelente calidad',
        'Horrible atención al cliente, no volveré',
        'Muy contento con la compra',
        'Esto es una estafa, pésima experiencia',
        'Producto perfecto, super recomendado',
        'Mala calidad, llegó roto'
    ],
    'sentimiento': ['positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'negativo']
})

def palabras_frecuentes_por_sentimiento(df):
    stop_words = set(stopwords.words('spanish'))

    # Diccionarios para contar
    positivos = Counter()
    negativos = Counter()

    for _, fila in df.iterrows():
        # palabras = word_tokenize(fila['texto'].lower())
        palabras = re.findall(r'\b\w+\b', fila['texto'].lower())
        filtradas = [p for p in palabras if p.isalpha() and p not in stop_words]
        if fila['sentimiento'] == 'positivo':
            positivos.update(filtradas)
        else:
            negativos.update(filtradas)

    print("\nPalabras más frecuentes en opiniones POSITIVAS:")
    print(positivos.most_common(5))

    print("\nPalabras más frecuentes en opiniones NEGATIVAS:")
    print(negativos.most_common(5))

palabras_frecuentes_por_sentimiento(data)
