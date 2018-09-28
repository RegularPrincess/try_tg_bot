import re
import telebot.types as types


def get_keyboard(list_btns):
    markup = types.ReplyKeyboardMarkup(row_width=len(list_btns))
    for i in list_btns:
        itembtn = types.KeyboardButton(i)
        markup.add(itembtn)
    if len(list_btns) < 1:
        return types.ReplyKeyboardRemove(selective=False)
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


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class User:
    def __init__(self):
        self.answs = []
        self.question = None
        self.is_last_quest = False
        self.q_index = 0


class Question:
    def __init__(self, text=None, answers=None):
        self.text = text
        if answers is None:
            self.answers = []
        else:
            self.answers = answers

