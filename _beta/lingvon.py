from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import logging
import requests
import random
import json
from urllib.request import urlopen

answer_number = None
words = None
onGoing = False

#INTIALIZE CORPUS DATA
r = urlopen('http://122.32.167.22/lingvon/5000')
corpus_data = eval(r.read())

min_number = 0
max_number = len(corpus_data)

min_range = min_number
max_range = max_number

level = 1

def setRange(level):
    global min_range
    global max_range

    min_range = int((max_number/50)*(level - 1))
    max_range = int((max_number/50)*level)

    print(min_range)
    print(max_range)

streaks = 0

#INTIALIZE BOT
updater = Updater(token='520354923:AAELKZSqpPiNuGQBg5tPsFBH4_8m1Y_EE6Y')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def getRandomNumber():
    random_number = random.randint(min_number,max_range)
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

def start(bot, update):
    global answer_number
    global words
    global onGoing

    onGoing = True
    msg = ""

    bot.send_message(chat_id=update.message.chat_id, text="LINGVON beta 0.0.3")
    words = getWordSets(4)
    answer_number = random.randint(1,4)

    bot.send_message(chat_id=update.message.chat_id, text=str("\n* FRA) WORD : \"" + words[str(answer_number)]['french'] + "\" *"))
    bot.send_message(chat_id=update.message.chat_id, text=str("STREAK(S) : " + str(streaks) + "\n"))

    for i in words:
        msg = msg + str(i + " : " + str(words[i]['english'])) + "\n"
    
    bot.send_message(chat_id=update.message.chat_id, text=msg)


def showTyping():
    return "bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)"

def bot_main(bot, update):
    global level
    global streaks
    global onGoing

    raw_user_input = update.message.text
    userInput = raw_user_input.lower().split()
    print(userInput)

    if(onGoing == True):
        if(words[str(userInput[0])]['english'] == words[str(answer_number)]['english']):
            streaks = streaks + 1
            eval(showTyping())
            bot.send_message(chat_id=update.message.chat_id, text=str("👍 CORRECT 👍"))
            onGoing = False
        else:  
            bot.send_message(chat_id=update.message.chat_id, text=str("😓 WRONG 😓"))
            bot.send_message(chat_id=update.message.chat_id, text=str("\n* \"" + words[str(userInput[0])]['english'] + '\" means \"' + words[str(userInput[0])]['french']+ "\" *"))
            streaks = 0
    elif(userInput[0] == "level"):
        level = int(userInput[1])
        setRange(level)
        print(str(level))
    else:
        print(userInput[0])
        
            
def main():
    start_handler = CommandHandler('start', start)
    input_handler = MessageHandler(Filters.text, bot_main)
    
    dp = updater.dispatcher

    dp.add_handler(start_handler)
    dp.add_handler(input_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()


'''#606030525:AAEFUVRaI5LoaezwwS1YV_CazXPoJS-k4Bk

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import requests
from pprint import pprint

weather_token = '99c6f94afac6ff2e3b407e029c8de3a7'

updater = Updater(token='606030525:AAEFUVRaI5LoaezwwS1YV_CazXPoJS-k4Bk')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def getCelsius(kelvin):
    result = kelvin - 273.15
    return result

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm tyrone, lemme tell you the weather?")
    bot.send_message(chat_id=update.message.chat_id, text="where is you at?")

def tim(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm tim!")

def bot_main(bot, update):
    raw_user_input = update.message.text
    userInput = raw_user_input.split()
    print(userInput)

    msg = "default"

    if(userInput[0] == 'weather'):
        if(len(userInput) > 1):
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ userInput[1] + '&APPID='+ weather_token)

            weather_info = r.json()
            print(weather_info)

            if(weather_info['cod'] == 200):
                kelvin_temp = weather_info['main']['temp']
                celsius = getCelsius(kelvin_temp)
                msg = "about " + str(round(celsius)) + "°C"
            else:
                msg = "there ain't no city like that you dumbass"
    else:
        msg = userInput
        
    bot.send_message(chat_id=update.message.chat_id, text=str(msg))

def main():
    start_handler = CommandHandler('start', start)
    input_handler = MessageHandler(Filters.text, bot_main)
    
    dp = updater.dispatcher

    dp.add_handler(start_handler)
    dp.add_handler(input_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()'''
