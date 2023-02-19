from HanTa import HanoverTagger as ht
from os import listdir
from os.path import isfile, join
import os
import spacy
from nltk.tokenize import word_tokenize
import time

nlp = spacy.load("de_core_news_lg")


tagger = ht.HanoverTagger('morphmodel_ger.pgz')


dataset_dir = 'iwv_dataset_parsed/'
leichte_sprache_dataset = os.path.join(dataset_dir, "markdown_leichte_sprache/")
standard_sprache_dataset = os.path.join(dataset_dir, "markdown_standard/")

tagged_dir = 'tagged_dataset_hannovertagger/'
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
            tokenized = word_tokenize(text)
            tag_count = {}
            tagged = ""
            for token in tokenized:
                tag = tagger.tag_word(token)[0][0]
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
                tagged += f"({token}/{tag})"
                tagged += " "
            tagged += "\n\n"
            for tag in tag_count:
                tagged += f"{tag}: {tag_count[tag]}\n"

            with open(join(output_dir, file), 'w') as f:
                f.writelines(tagged)
            if index % 100 == 0:
                print(index)
            index += 1
        except Exception as e:
            print(e)
            print(f"Error in file {file}")
            continue

# start = time.time()

# tag_dir(leichte_sprache_dataset, tagged_leicht)
# leicht_end = time.time()


# tag_dir(standard_sprache_dataset, tagged_standard)
# standard_end = time.time()
# end = time.time()

# print("Time for leichte sprache: ", leicht_end - start)
# print("Time for standard sprache: ", standard_end - leicht_end)

# print("endtime: ", end - start)

# print tagset of the hannovertagger
print(tagger.list_postags())
print(tagger.list_mtags())