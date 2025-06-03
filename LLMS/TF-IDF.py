import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

# 1. Dataset (puedes reemplazar esto por un CSV propio)
data = {
    "texto": [
        "Me encantó el producto, muy bueno",
        "Pésimo servicio, no volveré",
        "Increíble calidad, 100 porciento recomendado",
        "Horrible experiencia, muy mala atención",
        "Excelente compra, llegó a tiempo",
        "No sirve, es una estafa",
    ],
    "sentimiento": [1, 0, 1, 0, 1, 0]  # 1 = positivo, 0 = negativo
}
df = pd.DataFrame(data)

# 2. Dividir datos
X_train, X_test, y_train, y_test = train_test_split(df["texto"], df["sentimiento"], test_size=0.3, random_state=42)

# 3. Vectorizar con TF-IDF
spanish_stopwords = stopwords.words('spanish')
vectorizer = TfidfVectorizer(stop_words=spanish_stopwords)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 4. Entrenar modelo
modelo = MultinomialNB()
modelo.fit(X_train_tfidf, y_train)

# 5. Evaluar
y_pred = modelo.predict(X_test_tfidf)
print("Precisión del modelo:", accuracy_score(y_test, y_pred))

# 6. Probar con una frase nueva
frase_nueva = ["Es un excelente producto"]
frase_vec = vectorizer.transform(frase_nueva)
print("Sentimiento:", modelo.predict(frase_vec)[0])  # 1 = positivo, 0 = negativo
