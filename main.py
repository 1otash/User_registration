# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from datetime import date, datetime
import telebot
import buttons
from telebot import types

import database

bot = telebot.TeleBot('6451761855:AAHwi8EiMTnXGqYJaYD0BLMT6KK7rZ3D32s')

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    checker = database.check_user(user_id)
    if checker:
        bot.reply_to(message, "You have already registered")
    else:
        bot.send_message(user_id, 'Type your full name')

@bot.message_handler(content_types=['text'])
def get_name(message):
    user_id = message.from_user.id
    username = message.text


    bot.send_message(user_id, "Send your phone number", reply_markup=buttons.number_buttons())
    bot.register_next_step_handler(message, get_number, username)


def get_number(message, username):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        bot.send_message(user_id, "Send your location", reply_markup=buttons.geo_buttons())
        bot.register_next_step_handler(message, location, username, phone_number)
    elif not message.contact:
        bot.send_message(user_id, 'Send your phone number by clicking a button', reply_markup=buttons.number_buttons())

        # Обратно на этап получения номера
        bot.register_next_step_handler(message, get_number, username)

def location(message, username, phone_number):
    user_id = message.from_user.id
    if message.location:
        user_location = message.location
        bot.send_message(user_id, 'Send your date of birthday like this. Example: 1997-10-22', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, date_birth, username, phone_number, user_location)
    else:
        bot.send_message(user_id, 'Отправьте локацию через кнопку!')
        bot.register_next_step_handler(message, location, username, phone_number)

def date_birth(message, username, phone_number, user_location):
    user_id = message.from_user.id
    if message.text:
        date_birthday = message.text
        database.register_user(user_id, username, phone_number)
        id_message = bot.send_message(user_id, f"You successfully registered {username}", reply_markup=types.ReplyKeyboardRemove())
        bot.reply_to(id_message, f'New application!\nИмя:{username}\n'
                                 f'Phone number:{phone_number}\n'
                                 f'Location:{user_location}\n'
                                 f'Birthday:{date_birthday}\n')
    else:
        bot.send_message(user_id, 'Send your date of birthday like this. Example: 10-10-1997', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, date_birth)






bot.infinity_polling()
