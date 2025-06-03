import spacy

# Cargar el modelo en español (o inglés si prefieres)
nlp = spacy.load("es_core_news_sm")  # Cambia a "en_core_web_sm" si prefieres inglés

texto = "Apple está buscando comprar una startup en España por 1 billón de dólares."
doc = nlp(texto)

# Imprimir tokens y sus etiquetas
for token in doc:
    print(token.text, "|", token.pos_, "|", token.lemma_)

# Entidades nombradas
for ent in doc.ents:
    print(ent.text, "-", ent.label_)
