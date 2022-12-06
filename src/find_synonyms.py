import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')


def synonym_extractor(word: str) -> set:
    return {l.name() for syn in nltk.corpus.wordnet.synsets(word) for l in syn.lemmas()}