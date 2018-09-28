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


def del_uid_from_dict(uid, dict_):
    if uid in dict_:
        del dict_[uid]


class User:
    def __init__(self):
        self.name = None
        self.city = None
        self.detail = None
        self.email = None


