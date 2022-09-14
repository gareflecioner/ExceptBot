https://mastergroosha.github.io/aiogram-2-guide/buttons/   про кнопки 
https://habr.com/ru/post/321510/                        про бд и коннект
https://off-bot.ru/threads/981/ sqlite and aiogram

Не работает 
CREATE DATABASE bd;
CREATE TABLE books("Id" BIGSERIAL PRIMARY KEY,
"Title" VARCHAR(50) NOT NULL,
"Author" VARCHAR NOT NULL,
"Year" INTEGER);
INSERT INTO books(
Title, Author, Year)
VALUES ("War and peace","Tolstoy","1863"),
("Crime and punishment","Dostoevsky","1866"),
("Teresa Zboncak","Vandervort","1556"),
("Luis Tromp", "Mills","1756"),
("Wilhelm Romaguera","Harber","456"),
("Hans Mann","O'Keefe","1986"),
("Misael Ortiz","Mann","1256"),
("Genry Genius","About","1454");
SELECT * FROM books



Рабочая бд

CREATE TABLE books (
  Id BIGSERIAL PRIMARY KEY,
  Название TEXT NOT NULL,
  Автор TEXT NOT NULL
);
INSERT INTO books VALUES (0001, 'Мы', 'Замятин');
INSERT INTO books VALUES (0002, 'Вино из одуванчиков', 'Брэдбери');
INSERT INTO books VALUES (0003, 'Парфюмер', 'Зюскинд');
INSERT INTO books VALUES (0004, 'Обелиск', 'Быков');
INSERT INTO books VALUES (0005, 'Тошнота', 'Сартр');
INSERT INTO books VALUES (0006, 'Коллекционер', 'Фаулз');
INSERT INTO books VALUES (0007, 'Над пропастью во ржи', 'Сэлинджер');
INSERT INTO books VALUES (0008, 'Пролетая над гнездом кукушки', 'Кизи');
INSERT INTO books VALUES (0009, 'Мертвые души', 'Гоголь');
INSERT INTO books VALUES (00010, 'Раковый корпус', 'Солженицин');
SELECT * FROM books 

https://dev-gang.ru/article/rabota-s-postgresql-v-python-xn8721sq0g/

Сперва установить библиотеку  pip3 install psycopg2
import psycopg2

con = psycopg2.connect(
  database="бд", 
  user="мой ник", 
  password="ага", 
  host="127.0.0.1", 
  port="5432"
)

print("Database opened successfully")

 https://ru.stackoverflow.com/questions/1285541/Как-сделать-запрос-к-Базе-Данных-из-Телеграм-бота-по-кнопке

https://thecode.media/python-bot/  Про обработчик кнопок   https://ejudge.179.ru/tasks/python/theory/24-telegram.html тоже есть информация про клавиатуру






хз


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
  if message_text =='text':
      bot.send_message(message.chat.id, "тут будет поиск", replay_markup=markup)
 item2=types.InlineKeyboardButton("Посмотреть аннотацию")
@bot.message_handler(content_types='text')
def description(message):
  if message_text=='text':
      bot.send_message(message.chat.id, "Тут будет аннотация", replay_markup=markup)
      item3=types.InlineKeyboardButton("Популярное")
@bot.message_handler(content_types='text')
def charts(message):
  if message_text=='text':
     bot.send_message(message.chat.id, "www.chitai-gorod.ru/article/glavnyye_bestsellery_goda/", replay_markup=markup)
item4=types.InlineKeyboardButton("Помощь")
@bot.message_handler(content_types='text')
def help(message):
  if message_text=='text':
      bot.send_message(message.chat.id, "Что-то пошло не так? Попробуйте связаться со мной!\nvk.com/gareflecioner", replay_markup=markup)
      markup.add(item1,item2)
      markup.add(item3,item4)
      bot.send_message(message.chat.id,"Сделай выбор!",reply_markup=markup)
      bot.polling(none_stop=True, interval=0)
