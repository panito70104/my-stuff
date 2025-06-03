from transformers import pipeline

# Cargar un modelo multilingüe o en español
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

resultado = sentiment_pipeline("Me gustan mucho los perritos y los gatos")
print(resultado)
