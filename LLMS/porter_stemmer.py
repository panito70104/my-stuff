from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

texto = "Studies studying cries cried flying flies"
tokens = word_tokenize(texto.lower())

stemmer = PorterStemmer()
stems = [stemmer.stem(palabra) for palabra in tokens]

print(stems)
# Output: ['studi', 'studi', 'cri', 'cri', 'fli', 'fli']