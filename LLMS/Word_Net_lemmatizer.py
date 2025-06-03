from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')

texto = "Studies studying cries cried flying flies"
tokens = word_tokenize(texto.lower())

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(palabra) for palabra in tokens]

print(lemmas)
# Output: ['study', 'study', 'cry', 'cry', 'fly', 'fly']