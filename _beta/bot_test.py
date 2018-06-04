
import telegram
bot = telegram.Bot(token='520354923:AAELKZSqpPiNuGQBg5tPsFBH4_8m1Y_EE6Y')

with open('./data/5000.json', encoding="utf-8") as f:
    corpus_data = json.load(f)

updates  = bot.get_updates(timeout=30)


chat_id = bot.get_updates()[-1].message.chat_id

bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)

bot.send_message(chat_id=chat_id, text="département")
print("département")
