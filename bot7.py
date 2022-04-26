import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('▶️Анекдот')
    item2 = types.KeyboardButton('⏺️Добавить анекдот')

    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, "Приветствую! Я бот-анекдот! Вы можете получить рандомный анекдот из моей коллекции, а также добавить в нее свой! ", parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '▶️Анекдот':
            file1 = open('anek.txt', 'r', encoding='utf-8')
            content = file1.readlines()
            file1.close()
            b = random.choice(content)
            bot.send_message(message.chat.id, b)
        elif message.text == '⏺️Добавить анекдот':
            bot.send_message(message.chat.id, 'Напишите сюда свой !небольшой! анекдот одной строкой ')
        elif message.text != '⏺️Добавить анекдот' and message.text != '▶️Анекдот' and message.text != '/start':
            user_anek = message.text
            with open('anek.txt', 'a', encoding='utf-8') as output:
                print(user_anek, file=output)    
bot.polling(none_stop=True)
