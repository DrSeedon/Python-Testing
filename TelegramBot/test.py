import telebot

bot = telebot.TeleBot('5888540829:AAFfHDp4dOsM2SQV0GL3jvRBcedgQ013Hxk')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(
        message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    mess = message

    if message.text == 'hi':
        mess = 'Hi'
    elif message.text == 'id':
        mess = message.from_user.id
    elif message.text == 'debug':
        mess = message
    elif message.text == 'photo':
        photo = open('photo.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        mess = 'I dont understand you'

        bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    mess = message

    if message.text == 'hi':
        mess = 'Hi'
    elif message.text == 'id':
        mess = message.from_user.id
    elif message.text == 'debug':
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'photo':


bot.polling(none_stop=True)
