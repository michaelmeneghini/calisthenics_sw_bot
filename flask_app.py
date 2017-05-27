from flask import Flask, request
import telepot
import urllib3
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
"""
# pythonanywhere stuff
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (
urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of pythonanywhere stuff
"""
secret = "b6612fe7-5ea6-444d-a315-e3f21faa2b39"
# connecting to Telegram
bot = telepot.Bot('343392414:AAECRTAnbVpxr9__x-gdfCUpwwIf3pAcLJs')
bot.setWebhook("https://cd08e219.ngrok.io/{}".format(secret), max_connections=1)

# creating a flask application
app = Flask(__name__)

#skills list that I'll need later
skills = ["Basics","Front Lever","Planche"]

levels = ["Beginner","Intermediate","Advanced"]

#variable that I need to store the skill that user wantsm in order to retrieve the right level routine for THAT skill
chosen_skill = ""

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    # json data (sent by Telegram) to a Python dictionary
    update = request.get_json()

    # handling commands
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]

        if text == "/test":
            bot.sendMessage(chat_id, "The bot is responding!")
            return "OK"

        elif text == "/routines":
            #matrix for keyboard buttons
            #TODO: add other skills
            #TODO: keep updated the skills list and the handleSkillRequest method too!
            skills_keyboard = [[KeyboardButton(text="Basics")],[KeyboardButton(text="Front Lever")], KeyboardButton(text="Planche")]
            bot.sendMessage(chat_id, "Choose a skill,", reply_markup=ReplyKeyboardMarkup(skills_keyboard))

        elif text in skills:
            chosen_skill = text
            levels_keyboard = [[KeyboardButton(text="Beginner")], [KeyboardButton(text="Intermediate")],KeyboardButton(text="Advanced")]
            bot.sendMessage(chat_id, "Choose your level,", reply_markup=ReplyKeyboardMarkup(levels_keyboard))

        elif text in levels:
            handleLevelRequest(text, chat_id)

        # default echo response
        else:
            bot.sendMessage(chat_id, "Echo: {}".format(text))
            return "OK"

def handleLevelRequest(level, chat):
    if level == "Beginner":
        bot.sendMessage(chat, "Beginner routine for chosen skill")
        #send beginner routine for chosen routine
    elif level == "Intermediate":
        bot.sendMessage(chat, "Intermediate routine for chosen skill")
    #advanced
    else:
        bot.sendMessage(chat, "Advanced routine for chosen skill")
    chosen_skill = ""









