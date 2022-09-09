import telebot
from telebot import types
token="5761808205:AAHOzoT6V-9ZO4pZ7Vecw7HPlqVXiFDZ4gw"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def ye(message):
    markup=types.ReplayKeyboardMarkup(resize_keyboard=True)
    button1=types.KeyboardButton("Просто кнопка1", replay_markup=markup)
    button2=types.KeyboardButton("Просто кнопка2", replay_markup=markup)
    markup.add(button1,button2)
    bot.send_message(message.chat.id,"Выбери что-нибудь",reply_markup=markup)
@bot.message_handler(content_types=["text"])
def ey(message):
    if(message.text=="Просто кнопка1"):
        bot.send_message(message.chat.id,"Будь добр,выбери кнопку2 ,ок")
    elif(message.text=="Просто кнопка2"):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button3=types.KeyboardButton("Просто кнопка3", replay_markup=markup)
        button4 = types.KeyboardButton("Просто кнопка4", replay_markup=markup)
        button5 = types.KeyboardButton("возврат к кнопкам 1,2", replay_markup=markup)
        markup.add(button3, button4,button5)
        bot.send_message(message.chat.id, "Будь добр еще раз ,ок")
    elif(message.text=='Просто кнопка3'):
        bot.send_message(message.chat.id, 'ок3')
    elif (message.text == 'Просто кнопка4'):
        bot.send_message(message.chat.id, 'ок4')
    elif(message.text=="возврат к кнопкам 1,2"):
        markup = types.ReplayKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("Просто кнопка1", replay_markup=markup)
        but2 = types.KeyboardButton("Просто кнопка2", replay_markup=markup)
        markup.add(but1, but2)
        bot.send_message(message.chat.id, "Тф вернулся,ок", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Joke")
    bot.polling(none_stop=True)


