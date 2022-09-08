
import telebot
from telebot import types
token='5684309043:AAFwX79gYjvDDxTay466K-Qg_Z9tomVRLy0'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
 markup=types.InlineKeyboardMarkup(resize_keyboard=True)
 item1=types.InlineKeyboardButton("Начать поиск на сайте ")
 @bot.message_handler(content_types='text')
 def search(message):
  if message =='text':
      bot.send_message(message.chat.id, "тут будет поиск", replay_markup="markup")
 item2=types.InlineKeyboardButton("Посмотреть аннотацию")
@bot.message_handler(content_types='text')
def description(message):
  if message=='text':
      bot.send_message(message.chat.id, "Тут будет аннотация", replay_markup="markup")
      item3=types.InlineKeyboardButton("Популярное")
@bot.message_handler(content_types='text')
def charts(message):
  if message=='text':
     bot.send_message(message.chat.id, "www.chitai-gorod.ru/article/glavnyye_bestsellery_goda/", replay_markup="markup")
item4=types.InlineKeyboardButton("Помощь")
@bot.message_handler(content_types='text')
def help(message):
  if message=='text':
      bot.send_message(message.chat.id, "Что-то пошло не так? Попробуйте связаться со мной!\nvk.com/gareflecioner", replay_markup="markup")
      "markup".add("item1","item2")
      "markup".add("item3","item4")
      bot.send_message(message.chat.id,"Сделай выбор!",reply_markup="markup")
      bot.polling(none_stop=True, interval=0)