import nltk
from nltk.tokenize import word_tokenize
from os import listdir
from os.path import isfile, join
import os
import time

nltk.download('averaged_perceptron_tagger')


dataset_dir = 'iwv_dataset_parsed/'
leichte_sprache_dataset = os.path.join(dataset_dir, "markdown_leichte_sprache/")
standard_sprache_dataset = os.path.join(dataset_dir, "markdown_standard/")

tagged_dir = 'tagged_dataset_nltk/'
tagged_leicht = join(tagged_dir, "leicht/")
tagged_standard = join(tagged_dir, "standard/")

def tag_dir(directory_to_tag, output_dir):
    files_to_tag = [f for f in listdir(directory_to_tag) if isfile(join(directory_to_tag, f))]
    index = 0
    for file in files_to_tag[:1000]:
        try:
            filepath = join(directory_to_tag, file)
            with open(filepath, 'r') as f:
                text = "".join(f.readlines())
                f.close()
            tagged = nltk.pos_tag(word_tokenize(text))
            with open(join(output_dir, file), 'w') as f:
                f.writelines(str(tagged))
                f.close()
            if index % 100 == 0:
                print(index)
            index += 1
        except Exception as e:
            print(e)
            print("Error with file: ", file)
            continue

start = time.time()
tag_dir(leichte_sprache_dataset, tagged_leicht)
leicht_end = time.time()
tag_dir(standard_sprache_dataset, tagged_standard)
standard_end = time.time()

end = time.time()
print("Leicht Sprache: ", leicht_end - start)
print("Standard sprache: ", standard_end - leicht_end)
print("Komplett: ", end - start)