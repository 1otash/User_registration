from telebot import types
def number_buttons():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    num_button = types.KeyboardButton('Поделиться контактом', request_contact=True)

    buttons.add(num_button)

    return buttons


def geo_buttons():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    g_button = types.KeyboardButton('Поделиться локацием', request_location=True)

    buttons.add(g_button)

    return buttons


