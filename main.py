import telebot
import telebot.types as types


bot = telebot.TeleBot("645100799:AAHr08yGqhY8PxAjeSJSdPiUZ-D2MgcB3i8")



# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.from_user.id, "Здравствуйте, вас приветствует тестовый бот, "
                                           "который поможет вам опросить клиентов. ")
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Да')
    itembtn2 = types.KeyboardButton('Нет')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.from_user.id, "Вам будет задан ряд вопросов, вы готовы?", reply_markup=markup)



@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Да" or message.text == "да":
        bot.send_message(message.from_user.id, "Hello! I am HabrahabrExampleBot. How can i help you?")

    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")

    else:
        bot.send_message(message.from_user.id, "Sorry, i dont understand you.")


bot.polling(none_stop=True, interval=0)

# Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass

bot.polling(none_stop=True, interval=0)