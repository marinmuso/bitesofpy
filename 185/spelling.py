from difflib import SequenceMatcher
from os import path
from urllib.request import urlretrieve


DICTIONARY = path.join('/tmp', 'dictionary.txt')
if not path.isfile(DICTIONARY):
    urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


def load_words():
    """Return a set of words from DICTIONARY"""
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()
    suggestion, top_ratio = None, 0
    for word in words:
        seq_matcher = SequenceMatcher(None, misspelled_word, word)
        ratio = seq_matcher.ratio()
        if ratio > top_ratio:
            top_ratio = ratio
            suggestion = word
    return suggestion

    