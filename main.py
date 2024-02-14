import telebot
from telebot import types as t
import random, Wiki



token = "6759921405:AAHpx_ohyMjxnj94Ot4XCOKW3PUyfA3qU2g"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["wiki"])
def wiki_start(message):
    b = bot.send_message(message.chat.id, "Напишите слово про которое хотите узнать подробнее")
    bot.register_next_step_handler(b, wiki_result)

def wiki_result(message):
    text = Wiki.get_wiki(message.text)
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["test"])
def testing(message):
    bot.send_message(message.chat.id, "Hello, my name Scarlet_Devil!")

@bot.message_handler(commands=["game"])
def paper_scissor_stone(message):
    bot.send_message(message.chat.id, "Давай поиграем в Камень-Ножницы-Бумага! Выбирай! ",
                     reply_markup=markup_for_game())

def markup_for_game():
    markup = t.InlineKeyboardMarkup()
    stone = t.InlineKeyboardButton(text="Камень", callback_data="Stone")
    scissor = t.InlineKeyboardButton(text="Ножницы", callback_data="Scissor")
    paper = t.InlineKeyboardButton(text="Бумага", callback_data="Paper")
    markup.add(stone, scissor, paper)
    return markup

@bot.callback_query_handler(lambda call:True)
def check(call):
    b = choice_bot()
    bot.send_message(call.message.chat.id, f"Бот выбрал: {b}")
    if call.data == b:
        bot.send_message(call.message.chat.id, f"Ничья... Давай заново!")
    elif call.data == "Paper" and b == "Stone":
        bot.send_message(call.message.chat.id, f"Перемога!")
    elif call.data == "Scissor" and b == "Paper":
        bot.send_message(call.message.chat.id, f"Перемога!")
    elif call.data == "Stone" and b == "Scissor":
        bot.send_message(call.message.chat.id, f"Перемога!")
    else:
        bot.send_message(call.message.chat.id, f"Поразка")
def choice_bot():
    list = ["Stone", "Paper", "Scissor"]
    num = random.randint(0, 2)
    return list[num]

@bot.message_handler(content_types=["text", "sticker"])
def echo_bot(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
