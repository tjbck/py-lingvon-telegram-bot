import random
import json
from urllib.request import urlopen

'''with open('./data/5000.json', encoding="utf-8") as f:
    corpus_data = json.load(f)'''

r = urlopen('http://122.32.167.22/lingvon/5000s')
s_corpus_data = eval(r.read())

r = urlopen('http://122.32.167.22/lingvon/5000')
corpus_data = eval(r.read())

'''min_number = 0
max_number = len(corpus_data)

level = 1

min_number = int((max_number/50)*(level - 1))
max_number = int((max_number/50)*level)

def getRandomNumber():
    random_number = random.randint(min_number,max_number)
    return random_number

def getWordData(number):
    word = corpus_data[number]
    return word

def getWordSets(number):
    words = {}
    for i in range(number):
        word_number = getRandomNumber()
        word = getWordData(word_number)
        word['number'] = word_number
        words[str(i + 1)] = word
    return words

RN = getRandomNumber()

FR = corpus_data[RN]['french']
EN = corpus_data[RN]['english']
print(FR)
print(EN)

FR = mot'''

f = open('./_beta/data/a.txt','a', encoding="utf-8")

w_count = 0
for w in corpus_data:
    w_count = w_count + 1
    FR = w['french']
    count = 0
    one_s = 'None'
    for s in s_corpus_data:
        if(FR in s['french'].split()):
            one_s = s
            count = count + 1


    txt = (FR + " : " +str(count) + " / "+ str(one_s) + "\n") 
    f.write(txt)
    #print(txt)

    prstg = w_count/len(corpus_data)
    print(str(prstg*100))