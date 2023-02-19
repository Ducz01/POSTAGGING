import spacy
from os import listdir
from os.path import isfile, join
import os
import time


nlp = spacy.load("de_core_news_lg")
dataset_dir = 'iwv_dataset_parsed/'
leichte_sprache_dataset = os.path.join(dataset_dir, "markdown_leichte_sprache/")
standard_sprache_dataset = os.path.join(dataset_dir, "markdown_standard/")

tagged_dir = 'tagged_dataset_spacy_de_core_news_lg/'
tagged_leicht = join(tagged_dir, "leicht/")
tagged_standard = join(tagged_dir, "standard/")


def tag_dir(directory_to_tag, output_dir):
    files_to_tag = [f for f in listdir(directory_to_tag) if isfile(join(directory_to_tag, f))]
    index = 0
    
    for file in files_to_tag:
        try:
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
            if index % 100 == 0:
                print(index)
            index += 1
        except Exception as e:
            print(e)
            print(f"Error in file {file}")
            continue


start = time.time()

tag_dir(leichte_sprache_dataset, tagged_leicht)
leicht_end = time.time()


tag_dir(standard_sprache_dataset, tagged_standard)
standard_end = time.time()
end = time.time()

print("Time for leichte sprache: ", leicht_end - start)
print("Time for standard sprache: ", standard_end - leicht_end)

print("endtime: ", end - start)