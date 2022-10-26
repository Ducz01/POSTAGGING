import spacy
from os import listdir
from os.path import isfile, join
import os

nlp = spacy.load("de_core_news_sm")
dataset_dir = 'iwv_dataset_parsed/'
leichte_sprache_dataset = os.path.join(dataset_dir, "markdown_leichte_sprache/")
standard_sprache_dataset = os.path.join(dataset_dir, "markdown_standard/")

tagged_dir = 'tagged_dataset/'
tagged_leicht = join(tagged_dir, "leicht/")
tagged_standard = join(tagged_dir, "standard/")


def tag_dir(directory_to_tag, output_dir):
    files_to_tag = [f for f in listdir(directory_to_tag) if isfile(join(directory_to_tag, f))]

    for file in files_to_tag[:1]:
        filepath = join(directory_to_tag, file)
        with open(filepath, 'r') as f:
            text = "".join(f.readlines())
            f.close()
        doc = nlp(text)
        tagged = ""
        for token in doc:
            tagged += f"({token.orth_}/{token.pos_})"
            tagged += " "
        POS_counts = doc.count_by(spacy.attrs.POS)
        tagged += "\n\n"

        for k,v in sorted(POS_counts.items()):
            tagged += (f'{k:{4}}. {doc.vocab[k].text:{5}}: {v}')
            tagged += "\n"
        
        with open(join(output_dir, file), 'w') as f:
            f.writelines(tagged)

tag_dir(leichte_sprache_dataset, tagged_leicht)
tag_dir(standard_sprache_dataset, tagged_standard)