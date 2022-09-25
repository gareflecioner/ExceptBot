from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
import random
import datetime



API_TOKEN = '5761808205:AAHOzoT6V-9ZO4pZ7Vecw7HPlqVXiFDZ4gw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())




Storage=MemoryStorage()


class registration(StatesGroup):
    name=State()
    surname=State()
    age=State()
    address=State()
    number=State()




@dp.message_handler(commands=['start'])
async def send_start(message:types. Message):
    keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    keyboard3.add(types.KeyboardButton(text="Launch Bot"))

    await message.answer(text="Нажми кнопку!", reply_markup=keyboard3)

    @dp.message_handler(lambda message: message.text == "Launch Bot")
    async def without1(message: types.Message):

        await message.reply(
                         "\n Если хочешь попытать судьбу и сыграть в кости\n/bones"
                         "\nЕсли возникли вопросы \n/help"
                         "\nПолезные ссылки\n/url"
                         "\nКвазирегистрация\n/registration"
                         "\nТекущее время\n/datetime"
                         "\nОтправка фото\n/photo"
                         "\nЗапрос номера телефона\n/contact"
                         "\nВыбор кед Convers\n/Clothes", reply_markup=keyboard3)

@dp.message_handler(commands=["help"])
async def send_help(message:types.Message):
    await message.answer("В случае каких-либо проблем-прошу связаться со мной.\nЯ ВКонтакте: vk.com/gareflecioner")

@dp.message_handler(commands="url")
async def send_commands(message: types.Message):
    buttons1 = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com/gareflecioner/hello_world.git"),
        types.InlineKeyboardButton(text="FSM", url="https://lolz.guru/threads/3769612/")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons1)
    await message.answer("Выбери кнопку!\n", reply_markup=keyboard)

@dp.message_handler(commands="photo")
async def send_photo(message: types.Message):
    keyboard2 = types.InlineKeyboardMarkup()

    b1=types.InlineKeyboardButton(text="😍", callback_data="like")
    b2=types.InlineKeyboardButton(text="🤢",callback_data="dislike")
    keyboard2.add(b1,b2)
    await message.answer_photo(
                               photo='https://proprikol.ru/wp-content/uploads/2019/10/krasivye-kartinki-pandy-na-rabochij-stol-26.jpg',
                               caption='Panda?',
                               reply_markup=keyboard2)

@dp.callback_query_handler()
async def answer_photo(callback:types.CallbackQuery):
    if callback.data=="like":
        await callback.answer(text="Поздравляю!!\n✌️")
    await callback.answer("Не поздравляю! \n😿")


@dp.message_handler(commands=['contact'])
async def enter_contact(message: types.Message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

    keyboard1.add(types.KeyboardButton(text="Запросить контакт", request_contact=True))

    await message.answer("number ,please", reply_markup=keyboard1)


#попробовать занести в бд
#озать команду регистрации

@dp.message_handler(commands=['Clothes'])
async def get_clothes(message: types.Message):

    conn=sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM convers ORDER BY RANDOM() LIMIT 1;")
    result=cur.fetchone()[1]

    await bot.send_message(message.from_user.id,result)

@dp.message_handler(commands=["registration"])
async def send_registration(message:types.Message):
    await message.answer("Укажи свое имя!")
    await registration.name.set()

@dp.message_handler(state=registration.name)
async def state1(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    name=message.text
    try:
        if not name.isnumeric():
            if len(name)>=5:
                await state.update_data(name)
                await message.answer(text="Укажи свою Фамилию!")
                await registration.surname.set()
            else:
                await message.answer("Введите корректное имя")
                await registration.name.set()
        else:
            await message.answer('Введите имя без цифр!')
            await registration.name.set()
    except:
        await message.answer(text="Укажи свою Фамилию")
        await registration.surname.set()


@dp.message_handler(state=registration.surname)
async def state2(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)

    await message.answer(text="Сколько тебе лет?")
    await registration.age.set()

@dp.message_handler(state=registration.age)
async def state3(message:types.Message, state: FSMContext):
    await state.update_data(age=message.text)

    answer=message.text
    try:
        if answer.isnumeric():
            if int(answer)<100:
                await state.update_data(answer)
                await message.answer(text="Укажи свой номер телефона!")
                await registration.number.set()

            else:
                await message.answer("Введите корректный возраст")
                await registration.age.set()
        else:
                await message.answer("Введите корректный возраст")
                await registration.age.set()

    except Exception:
        await message.answer(text="Укажи свой домашний адрес")
        await registration.address.set()

@dp.message_handler(state=registration.address)
async def state4(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer(text="Укажи свой номер телефона")
    await registration.number.set()


@dp.message_handler(state=registration.number)
async def state5(message:types.Message, state: FSMContext):
    await state.update_data(number=message.text)


    data = await state.get_data()
    await message.answer(f"Ваше Имя: {data['name']}\n"
                         f"Ваша Фамилия: {data['surname']}\n"
                         f"Ваш возраст: {data['age']}\n"
                         f"Ваш домашний адрес: {data['address']}\n"
                         f"Ваш номер телефона: {data['number']}\n")

    await state.finish()


@dp.message_handler(commands=["datetime"])
async def send_datatime(message:types.Message):
    dt_now=datetime.datetime.now()
    await message.answer(dt_now)


@dp.message_handler(commands=["bones"])
async def send_bones(message:types.Message):
    random1 =["Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Ребро"]
    random2 =random.choice(random1)
    await message.answer(random2)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)