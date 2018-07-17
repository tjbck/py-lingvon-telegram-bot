with open('./lingvon/5000s.json', encoding="utf-8") as f:
    read_data = f.read()
print(read_data)
s_corpus_data = eval(read_data)


'''import csv
data = []
with open('_beta/data/s.csv', 'r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        english = (row[1][::-1][4:][::-1][2:][::-1][2:][::-1])
        french = (row[0][::-1][12:][::-1])
        data.append(str(french + "," + english + "\n"))

with open('_beta/data/m.csv','w') as file:
    for line in data:
        file.write(str(line))

for row in data:
    print(row)
import random
import json
from urllib.request import urlopen

r = urlopen('http://122.32.167.22/lingvon/5000')
corpus_data = eval(r.read())

min_number = 0
max_number = len(corpus_data)

level = 49

min_number = int((max_number/50)*(level - 1))
max_number = int((max_number/50)*level)

print(min_number)
print(max_number)'''

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