import pandas as pd

# Datos simples
data = {
    "texto": [
        "Me encantó la película",
        "La comida estuvo horrible",
        "Muy buen servicio",
        "No me gustó para nada",
        "Excelente atención",
        "Terrible experiencia",
        "Muy recomendable",
        "Una pérdida de tiempo"
    ],
    "sentimiento": ["positivo", "negativo", "positivo", "negativo", "positivo", "negativo", "positivo", "negativo"]
}

df = pd.DataFrame(data)

from sklearn.feature_extraction.text import CountVectorizer

# Convertir texto a vectores de frecuencia (BOW)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["texto"])

from sklearn.naive_bayes import MultinomialNB
# Entrenar el modelo
y = df["sentimiento"]
modelo = MultinomialNB()
modelo.fit(X, y)

# Frase nueva para predecir
negativa_frase = ["Me pareció terrible la película, no la recomendaría a nadie"]
positiva_frase = ["Me pareció increíble la película, la recomendaría a todos"]
X_nueva = vectorizer.transform(negativa_frase)
prediccion = modelo.predict(X_nueva)
print("Sentimiento:", prediccion[0])

X_nueva = vectorizer.transform(positiva_frase)
prediccion = modelo.predict(X_nueva)
print("Sentimiento:", prediccion[0])
