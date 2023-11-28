from telebot import types

def name_button():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    name = types.KeyboardButton('Add your name')
    buttons.add(name)
    return buttons

def number_buttons_ru():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    num_button = types.KeyboardButton('Поделиться контактом', request_contact=True)

    buttons.add(num_button)

    return buttons


def geo_buttons_ru():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    g_button = types.KeyboardButton('Поделиться локацием', request_location=True)

    buttons.add(g_button)

    return buttons

def number_buttons():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    num_button = types.KeyboardButton('Share number', request_contact=True)

    buttons.add(num_button)

    return buttons


def geo_buttons():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    g_button = types.KeyboardButton('Share location', request_location=True)

    buttons.add(g_button)

    return buttons

def lang():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    RU = types.KeyboardButton('RU')
    EN = types.KeyboardButton('EN')
    buttons.add(RU, EN)
    return buttons