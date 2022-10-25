import nltk
from nltk import word_tokenize

sentence = "Da steppt der Bär."


tokens = nltk.tokenize.WordPunctTokenizer().tokenize(sentence)
print(tokens)



print(nltk.word)


tagged = nltk.pos_tag(tokens)
print(tagged)