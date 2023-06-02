import telebot
from random import randrange
from tkinter import*
import random
from telebot import types
from scipy.spatial import KDTree




bot = telebot.TeleBot("6040382505:AAEF_E7aPzour15jMSCFo70uLzzAS_k5hEQ")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    mess = f"Привет, <b>{message.from_user.first_name}</b>. Этот бот находится в разработке, потерпи немного"
    bot.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Записаться")
    btn2 = types.KeyboardButton('Выбрать цвет')
    btn3 = types.KeyboardButton('Контакты')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Выбери, что хочешь сделать", reply_markup=markup)



@bot.message_handler()
def get_user_text(message):
    if message.text == 'Записаться':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://n780951.yclients.com/')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "По кнопке ниже можно записаться", reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Назад в меню")
        markup.add(btn5)
    elif message.text == 'Контакты':
        bot.send_message(message.chat.id, 'Адрес: ул. Ангарская, д.53, к.1(вход со стороны дороги) \nТелефон: 8(967) 192-91-35')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Назад в меню")
        markup.add(btn5)
    elif message.text == 'Выбрать цвет':
        bot.send_message(message.chat.id,'Наш бот дает вам информацию и отрендовых цветах по сезонам, а вы уже сами выбираете нужный оттенок из палитры')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("Старт")
        markup.add(btn4)
        bot.send_message(message.from_user.id, "Если вы готовы, нажмите кнопку старт", reply_markup=markup)

    elif message.text == 'Старт':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        sg1 = types.KeyboardButton("Лето")
        sg2 = types.KeyboardButton("Осень")
        sg3 = types.KeyboardButton("Весна")
        sg4 = types.KeyboardButton("Зима")
        btn5 = types.KeyboardButton("Назад в меню")
        markup1.add(sg1, sg2, sg3, sg4, btn5)
        bot.send_message(message.from_user.id,'Выберите время года', reply_markup=markup1)
    elif message.text == 'Лето':
        bot.send_message(message.chat.id, 'Пока не доступно')
    elif message.text == 'Осень':
        bot.send_message(message.chat.id, 'Пока не доступно')
    elif message.text == 'Весна':
        bot.send_message(message.chat.id, 'Трендовые цвета весны 2023:  мятный, фисташка, небесно-голубой, лавандовый, молочный, карамельный \n'
                                          'Главные цвета - персиково-розовый и огенно-красный\n'
                                          'Весна - прекрасное время года, но также и сезон сухости рук\n'
                                          'Попробуйте процедуру парафинотерапии по специальной цене - 400 рублей')
    elif message.text == 'Зима':
        bot.send_message(message.chat.id, 'Пока не доступно')

    else:
        bot.send_message(message.chat.id, 'Разработка', parse_mode='html')





bot.polling()
