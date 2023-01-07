from os import listdir
from os.path import isfile, join

def get_word_count(text: str):
    return len(text.split())


def tag_dir(directory_to_tag, output_path):
    files_to_tag = [f for f in listdir(directory_to_tag) if isfile(join(directory_to_tag, f))]
    words = ""
    for file in files_to_tag:
        filepath = join(directory_to_tag, file)
        with open(filepath, 'r') as f:
            text = f.readlines()
            for word in text:
                words += word
                if get_word_count(words) > 100000:
                    break
            f.close()
        if get_word_count(words) > 100000:
            break
        
    # write words to file 
    with open(join(output_path), 'w') as f:
        f.writelines(words)


tag_dir("iwv_dataset_parsed/markdown_leichte_sprache/", "words_leicht.txt")
tag_dir("iwv_dataset_parsed/markdown_standard/", "words_standard.txt")

