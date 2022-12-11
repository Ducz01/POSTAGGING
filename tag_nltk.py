import nltk
from nltk.tokenize import word_tokenize
from os import listdir
from os.path import isfile, join
import os

dataset_dir = 'iwv_dataset_parsed/'
leichte_sprache_dataset = os.path.join(dataset_dir, "markdown_leichte_sprache/")
standard_sprache_dataset = os.path.join(dataset_dir, "markdown_standard/")

tagged_dir = 'tagged_dataset_nltk/'
tagged_leicht = join(tagged_dir, "leicht/")
tagged_standard = join(tagged_dir, "standard/")

def tag_dir(directory_to_tag, output_dir):
    files_to_tag = [f for f in listdir(directory_to_tag) if isfile(join(directory_to_tag, f))]
    
    for file in files_to_tag:
        filepath = join(directory_to_tag, file)
        with open(filepath, 'r') as f:
            text = "".join(f.readlines())
            f.close()
        tagged = nltk.pos_tag(word_tokenize(text))
        with open(join(output_dir, file), 'w') as f:
            f.writelines(str(tagged))
            f.close()

tag_dir(leichte_sprache_dataset, tagged_leicht)
tag_dir(standard_sprache_dataset, tagged_standard)
