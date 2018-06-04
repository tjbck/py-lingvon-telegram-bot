




import random
import json
from urllib.request import urlopen

'''with open('./data/5000.json', encoding="utf-8") as f:
    corpus_data = json.load(f)'''

r = urlopen('http://122.32.167.22/lingvon/5000')
corpus_data = eval(r.read())

min_number = 0
max_number = len(corpus_data)

level = 49

min_number = int((max_number/50)*(level - 1))
max_number = int((max_number/50)*level)

print(min_number)
print(max_number)

'''def getRandomNumber():
    random_number = random.randint(min_number,max_number)
    return random_number

def getWordData(number):
    word = corpus_data[number]
    return word

def getWordSets(number):
    words = {}
    for i in range(number):
        word = getWordData(getRandomNumber())
        words[str(i + 1)] = word
    return words


print(getWordSets(3))'''