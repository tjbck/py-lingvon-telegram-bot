import random
import json
from urllib.request import urlopen

with open('./data/5000.json', encoding="utf-8") as f:
    corpus_data = json.load(f)

'''r = urlopen('http://122.32.167.22/lingvon/5000')
corpus_data = eval(r.read())'''

min_number = 0
max_number = len(corpus_data)

level = 2

min_number = int((max_number/50)*(level - 1))
max_number = int((max_number/50)*level)


streaks = 0

def getRandomNumber():
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

def wordtype():
    word = getWordData(getRandomNumber())

    print("french : "+word['french'] + "\n")

    while True:
        userInput = input("english : ")
        if(userInput == word['english']):
            print("correct")
            break
        elif(userInput == "0"):
            quit()
        else:
            print(word['english'] + "\n")  


def multipleChoice(how_many_choices):
    global streaks
    words = getWordSets(how_many_choices)
    answer_number = random.randint(1,how_many_choices)

    print("\n* ENG) WORD : \"" + words[str(answer_number)]['english'] + "\" *")
    print("STREAK(S) : " + str(streaks) + "\n")

    for i in words:
        print(i + " : " + words[i]['french'])

    while True:
        userInput = input("\nchoose one : ")
        if(words[str(userInput)]['french'] == words[str(answer_number)]['french']):
            print("\nCORRECT")
            streaks = streaks + 1
            break
        else:
            print("\n* \"" + words[str(userInput)]['french'] + '\" means \"' + words[str(userInput)]['english']+ "\" *")
            print("\nWRONG")
            streaks = 0

def multipleChoiceFra(how_many_choices):
    global streaks
    words = getWordSets(how_many_choices)
    answer_number = random.randint(1,how_many_choices)

    print("\n* FRA) WORD : \"" + words[str(answer_number)]['french'] + "\" *")
    print("STREAK(S) : " + str(streaks) + "\n")

    for i in words:
        print(i + " : " + str(words[i]['english']))

    while True:
        userInput = input("\nchoose one : ")
        if(words[str(userInput)]['english'] == words[str(answer_number)]['english']):
            print("\nCORRECT")
            streaks = streaks + 1
            break
        else:
            print("\n* \"" + words[str(userInput)]['english'] + '\" means \"' + words[str(userInput)]['french']+ "\" *")
            print("\nWRONG")
            streaks = 0

if __name__ == '__main__':
    while True:
        #wordtype()
        multipleChoiceFra(4)

 




'''
import requests
lingo_from = 'fra'
lingo_dest = 'eng'
from pprint import pprint
phrase = "l'"

r = requests.get('https://glosbe.com/gapi/translate?from=' + lingo_from + '&dest=' + lingo_dest + '&format=json&phrase=' + phrase +'&pretty=true')

lingo_info = r.json()

pprint(lingo_info)

print(lingo_info['tuc'][0]['meanings'][0]['text'])
print(lingo_info['tuc'][0]['phrase']['text'])
'''