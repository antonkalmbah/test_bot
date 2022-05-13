from setuptools import Command
import telebot
from telebot import types

TOKEN = '5145407960:AAEI_8DRW4V3O4TtUHHVTqGyPtnjk_Zul84'
bot = telebot.TeleBot(TOKEN)

# создаём декоратов и функцию, которая будет запускаться сразу при запуске бота
@bot.message_handler(commands=['start'])
def start(message):
    # создаём клавиатуру рядом с кнопкой "Вложить"
    keyboards_menu = types.ReplyKeyboardMarkup()
    # делаем кнопку
    button_menu = types.KeyboardButton('Начнём!')
    # добавляем кнопку в клавиатуру
    keyboards_menu.add(button_menu)
    # отображаем и нужно соблюдать порядок внизу с send_message, чтобы отображалось имя пользователя при ответе
    bot.send_message(message.chat.id, text = "Привет, {0.first_name}!".format(message.from_user), reply_markup=keyboards_menu)

@bot.message_handler(content_types=['text'])
def menu(message):
    if(message.text == 'Начнём!'):
        # создаём клавиатуру, отображаемую в самом чате
        keyboards_contact = types.InlineKeyboardMarkup()

        # делаю кнопки отдельно от функции, чтобы кнопки не дублировались
        button_telegram = types.InlineKeyboardButton(text='Telegram', url='https://t.me/antonkalmbah')
        keyboards_contact.add(button_telegram)

        # вторая кнопка
        button_vk = types.InlineKeyboardButton(text='VK', url='https://vk.com/antonkalmbah')
        keyboards_contact.add(button_vk)
        bot.reply_to(message, text = "Как со мной связаться: ", reply_markup=keyboards_contact)


bot.polling(non_stop=True)