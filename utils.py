import re
import telebot.types as types


def get_keyboard(list_btns):
    markup = types.ReplyKeyboardMarkup(row_width=len(list_btns) - 1)
    for i in list_btns:
        itembtn = types.KeyboardButton(i)
        markup.add(itembtn)
    return markup


def is_email_valid(email):
    match = re.fullmatch('[\w.-]+@\w+\.\w+', email)
    if match:
        return True
    else:
        return False


class User:
    def __init__(self):
        name = None
        city = None
        detail = None
        email = None


