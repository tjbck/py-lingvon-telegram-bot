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

    '''print(min_range)
    print(max_range)'''

streaks = 0

#INTIALIZE BOT
updater = Updater(token='609569578:AAELG9EulmmOJTYY8L1zgM7Oqcuf9Q3bHAc')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


#### EDIT CODES HERE ####

def getRandomNumber():
    random_number = random.randint(min_range,max_range)
    #print(random_number)
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

def start(bot, update):
    global onGoing

    bot.send_message(chat_id=update.message.chat_id, text="LINGVON beta 0.0.8")

    onGoing = False
    
    custom_keyboard = [['1', '2'],['3', '4']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat_id, text="TYPE ANY KEY TO START", reply_markup=reply_markup)

def bot_help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="✔ type 'level' to set level ✔")
    bot.send_message(chat_id=update.message.chat_id, text="✔ type 'lookup' to retrive word data ✔")


def showTyping():
    return "bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)"

def bot_main(bot, update):
    global level
    global onGoing
    global streaks
    global answer_number
    global words
    

    raw_user_input = update.message.text
    userInput = raw_user_input.lower().split()
    print(userInput)

    if(userInput[0] == "level"):
        level = int(userInput[1])
        setRange(level)
        print(str(level))
        bot.send_message(chat_id=update.message.chat_id, text=("🌟 LEVEL SET TO " + str(level) + " 🌟"))
        onGoing = False
        bot.send_message(chat_id=update.message.chat_id, text="TYPE ANY KEY TO RESTART")
        
    elif(userInput[0] == "lookup"):
        word_number = int(userInput[1])
        word = getWordData(word_number)
        bot.send_message(chat_id=update.message.chat_id, text=("🌐 WORD DATA 🌐\nFRA) " + str(word['french']) + " ENG) " + str(word['english']) + ""))

    else:
        #LEAVE IT AS IT IS
        if(onGoing == True):
            userInput = " ".join(userInput)
            if(str(userInput) == str(words[str(answer_number)]['english']).lower()):
                streaks = streaks + 1
                eval(showTyping())
                bot.send_message(chat_id=update.message.chat_id, text=str("👍 CORRECT 👍"))
                onGoing = False
            else:
                bot.send_message(chat_id=update.message.chat_id, text=str("😓 WRONG 😓"))
                for i in words:
                    if (words[i]['english'] == userInput):
                        bot.send_message(chat_id=update.message.chat_id, text=str("\n* \"" + str(userInput) + '\" is \"' + str(words[i]['french'])+ "\" in french *"))
                streaks = 0

        if(onGoing == False):
            onGoing = True
            words = getWordSets(4)
            answer_number = random.randint(1,4)

            bot.send_message(chat_id=update.message.chat_id, text=("#" + str(words[str(answer_number)]['number']) + " * LVL. " + str(level) + " FRA) WORD : \"" + words[str(answer_number)]['french'] + "\" *"), timeout=30)
            bot.send_message(chat_id=update.message.chat_id, text=("STREAK(S) : " + str(streaks) + "\n"))

            custom_keyboard = [[words["1"]['english'], words["2"]['english']],[words["3"]['english'], words["4"]['english']]]
            reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
            bot.send_message(chat_id=update.message.chat_id, text="CHOOSE ONE", reply_markup=reply_markup)

        
            
def main():
    
    print("STARTED")
    setRange(level)
    print("SET LEVEL TO " + str(level))
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', bot_help)
    input_handler = MessageHandler(Filters.text, bot_main)
    
    dp = updater.dispatcher

    dp.add_handler(start_handler)
    dp.add_handler(help_handler)
    dp.add_handler(input_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

