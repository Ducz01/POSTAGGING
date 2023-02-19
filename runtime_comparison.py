import spacy
from os import listdir
from os.path import isfile, join
import os
import time
import nltk
from nltk.tokenize import word_tokenize
import stanza
from HanTa import HanoverTagger as ht

# this script uses all models to tag the dataset consisting of 100.000 words for leichte and standard sprache and compares the runtime
def runtime_spacy():
    spacy_models = ["de_core_news_sm", "de_core_news_lg", "de_dep_news_trf"]

    leicht_path = "words_leicht.txt"
    standard_path = "words_standard.txt"

    def tag(model: str, category: str):
        spacy_model = spacy.load(model)
        path = f"words_{category}.txt"
        with open(path, 'r') as f:
            text = "".join(f.readlines())
            f.close()
        start = time.time()
        doc = spacy_model(text)
        end = time.time()
        return f"{model} - {category}: {end-start}"

    results = []
    for model in spacy_models:
        for category in ["leicht", "standard"]:
            results.append(tag(model, category))
    with open("results.txt", 'w') as f:
        f.writelines("\n".join(results))
        f.close()
def runtime_nltk():
    with open("words_leicht.txt", 'r') as f:
        leicht_text = "".join(f.readlines())
        f.close()
    start = time.time()
    tagged = nltk.pos_tag(word_tokenize(leicht_text))
    end = time.time()
    print(f"nltk - leicht: {end-start}")

    with open("words_standard.txt", 'r') as f:
        standard_text = "".join(f.readlines())
        f.close()
    start = time.time()
    tagged = nltk.pos_tag(word_tokenize(standard_text))
    end = time.time()
    print(f"nltk - standard: {end-start}")

def runtime_stanford():
    nlp = stanza.Pipeline('de')
    with open("words_leicht.txt", 'r') as f:
        leicht_text = "".join(f.readlines())
        f.close()
    start = time.time()
    doc = nlp(leicht_text)
    end = time.time()
    print(f"stanford - leicht: {end-start}")

    with open("words_standard.txt", 'r') as f:
        standard_text = "".join(f.readlines())
        f.close()
    start = time.time()
    doc = nlp(standard_text)
    end = time.time()
    print(f"stanford - standard: {end-start}")

def runtime_hannovertagger():
    tagger = ht.HanoverTagger('morphmodel_ger.pgz')
    with open("words_leicht.txt", 'r') as f:
        leicht_text = "".join(f.readlines())
        f.close()
    
    start = time.time()
    tokenized = word_tokenize(leicht_text)
    for token in tokenized:
        tag = tagger.tag_word(token)[0][0]
    end = time.time()
    print(f"hannovertagger - leicht: {end-start}")

    with open("words_standard.txt", 'r') as f:
        standard_text = "".join(f.readlines())
        f.close()
    start = time.time()
    tokenized = word_tokenize(standard_text)
    for token in tokenized:
        tag = tagger.tag_word(token)[0][0]
    end = time.time()
    print(f"hannovertagger - standard: {end-start}")

runtime_hannovertagger()