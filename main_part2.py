import spacy
from os import listdir
from os.path import isfile, join
import os
import time

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





