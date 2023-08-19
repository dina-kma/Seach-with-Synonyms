#pip3 install nltk from terminal

import nltk
nltk.download('wordnet')
nltk.download('punkt')
#The four lines above are necessary on the first time only

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
words = []
search = []
result = []
si = input('Search Item: ')
search.append(si)
words.append(si)
text = word_tokenize(si)
for word in text:
    search.append(word)
    syns = wordnet.synsets(word)
    for syn in syns:
        for l in syn.lemmas():
            search.append(l.name())
for i in search:
    with open(r'words.txt','r') as fp:
        lines = fp.readlines()
    for line in lines:
        if line.find(i) != -1:
            result.append(i)
print(set(result))
