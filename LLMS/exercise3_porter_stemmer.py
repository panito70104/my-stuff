from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
def porter_stemmer_example():
    texto = "Los niños estaban corriendo y gritando mientras jugaban"
    tokens = word_tokenize(texto.lower())

    stemmer = PorterStemmer()
    stems = [stemmer.stem(palabra) for palabra in tokens]

    print(stems)
# Output: ['los', 'niñ', 'estab', 'corr', 'y', 'grit', 'mientr', 'jug']

def word_net_lemmatizer_example():
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    import nltk

    nltk.download('wordnet')
    nltk.download('omw-1.4')

    texto = "Los niños estaban corriendo y gritando mientras jugaban"
    tokens = word_tokenize(texto.lower())

    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(palabra) for palabra in tokens]
    print(lemmas)
porter_stemmer_example()
word_net_lemmatizer_example()
# Output: ['los', 'niño', 'estaban', 'corriendo', 'y', 'gritando', 'mientras', 'jugar']