import telebot

from telebot import types

bot = telebot.TeleBot('SecretSecretSecretSecret')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуй, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Nice photo, bro!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Nice man", url="https://vk.com/16valveprioraman"))
    bot.send_message(message.chat.id, 'Links', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    cat = types.KeyboardButton('Cat')
    dog = types.KeyboardButton('Dog')
    markup.add(cat, dog)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def mess_animal(message):
    if message.text == 'Cat':
        photo = open('загрузка.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        photo = open('sobaka.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)


bot.polling(none_stop=True)