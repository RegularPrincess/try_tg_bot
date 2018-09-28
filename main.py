import telebot
import telebot.types as types
import utils as u


bot = telebot.TeleBot("645100799:AAHr08yGqhY8PxAjeSJSdPiUZ-D2MgcB3i8")
USERS = {}
ADMINS = []


def send_to_admins(user):
    for a in ADMINS:
        bot.send_message(a, "Пользователь {} прошел опрос. Его ответы: {}\n{}"
                         .format(user.name, user.city + ", " + user.detail, user.email))


# Обработчик команд '/start' и '/imadmin'.
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.from_user.id, "Здравствуйте, вас приветствует тестовый бот, "
                                           "который поможет вам опросить клиентов. ")
    markup = u.get_keyboard(["Да", "Нет"])
    bot.send_message(message.from_user.id, "Вам будет задан ряд вопросов, вы готовы?", reply_markup=markup)
    USERS[message.from_user.id] = u.User()


@bot.message_handler(commands=['imadmin'])
def handle_start_help(message):
    bot.send_message(message.from_user.id, "Теперь вы админ этого бота и "
                                           "будете получать информацию о пользователях прошедших опрос")
    ADMINS.append(message.from_user.id)


@bot.message_handler(commands=['imnotadmin'])
def handle_start_help(message):
    bot.send_message(message.from_user.id, "Теперь вы не админ этого бота")
    ADMINS.remove(message.from_user.id)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.lower() == "да":
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.from_user.id, "Введите ваше имя, пожалуйста", reply_markup=markup)

    elif USERS[message.from_user.id].name is None:
        USERS[message.from_user.id].name = message.text
        markup = u.get_keyboard(["Казань", "Бугульма", "Зеленодольск", "Альметьевск"])
        msg = "{}, выберите город доставки или введите свой вариант".format(USERS[message.from_user.id].name)
        bot.send_message(message.from_user.id, msg, reply_markup=markup)

    elif USERS[message.from_user.id].city is None:
        USERS[message.from_user.id].city = message.text
        bot.send_message(message.from_user.id, "Уточните улицу и дом")

    elif USERS[message.from_user.id].detail is None:
        USERS[message.from_user.id].detail = message.text
        markup = u.get_keyboard(["Пропустить"])
        msg = "Сообщите, пожалуйста, ваш email или вы можете пропустить этот шаг"
        bot.send_message(message.from_user.id, msg, reply_markup=markup)

    elif USERS[message.from_user.id].email is None:
        if message.text == "Пропустить":
            USERS[message.from_user.id].email = "Пропущено"
        elif u.is_email_valid(message.text):
            USERS[message.from_user.id].email = message.text
            markup = u.get_keyboard(["/start"])
            # markup = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(message.from_user.id, "Спасибо, за пройденный опрос", reply_markup=markup)
            send_to_admins(USERS[message.from_user.id])
            USERS[message.from_user.id] = u.User()
            # u.del_uid_from_dict(message.from_user.id, USERS)
        else:
            bot.send_message(message.from_user.id, "❗ Адрес электронной почты не распознан. "
                                                   "Введите, пожалуйста, в формате example@domain.ru")
    else:
        pass

#
# # Обработчик для документов и аудиофайлов
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_document_audio(message):
#     pass

bot.polling(none_stop=True, interval=0)
