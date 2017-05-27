# -*- coding: utf-8 -*-
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import telepot
import time

def handle(msg):
    text = msg["text"]
    chat_id = msg["chat"]["id"]

    if text == "/test":
        bot.sendMessage(chat_id, "The bot is responding!")
        return "OK"

    elif text == "/routines":
        #matrix for keyboard buttons
        #TODO: add other skills
        #TODO: keep updated the skills list and the handleSkillRequest method too!
        skills_keyboard = [[KeyboardButton(text="Basics")],[KeyboardButton(text="Front Lever")], [KeyboardButton(text="Planche")]]
        bot.sendMessage(chat_id, "Choose a skill", reply_markup=ReplyKeyboardMarkup(keyboard=skills_keyboard))

    elif text in skills:
        chosen_skill = text
        levels_keyboard = [[KeyboardButton(text="Beginner")], [KeyboardButton(text="Intermediate")],[KeyboardButton(text="Advanced")]]
        bot.sendMessage(chat_id, "Choose your level", reply_markup=ReplyKeyboardMarkup(keyboard=levels_keyboard))

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


#skills list that I'll need later
skills = ["Basics","Front Lever","Planche"]

levels = ["Beginner","Intermediate","Advanced"]

#variable that I need to store the skill that user wantsm in order to retrieve the right level routine for THAT skill
chosen_skill = ""

bot = telepot.Bot('343392414:AAECRTAnbVpxr9__x-gdfCUpwwIf3pAcLJs')

bot.message_loop(handle)
while 1:
    time.sleep(10)
