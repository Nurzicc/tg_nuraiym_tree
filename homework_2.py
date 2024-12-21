from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from button import keydord_main, MENU, generate_menu_keyboard
import asyncio
from config import token

bot = Bot(token=token)
dp = Dispatcher()

@dp.message (Command ("start"))
async def start (message:types.Message):
    await message.answer("Привет Добро пожаловать!",reply_markup=keydord_main)
    await message.answer('этот бот умеет ответить на ваши выбранные темы')

@dp.message (Command ("about"))
async def start (message:types.Message):
    await message.answer("""Привет! Я — информационный бот, созданный для того,
чтобы помочь тебе быстро получать информацию по различным вопросам. Я могу предоставить актуальные данные по таким темам, как:
Новости: Получай свежие новости по самым важным темам.
Курсы валют: Узнай актуальные курсы обмена валют, такие как доллар, евро и другие.
Контактная информация: Найди все контактные данные для связи с нашей компанией.
Часто задаваемые вопросы (FAQ): Ответы на наиболее часто задаваемые вопросы о боте и его функционале""")
    
@dp.message (Command ("help"))
async def start (message:types.Message):
    await message.answer("""Привет! Я — информационный бот, который помогает тебе получить информацию по разнообразным темам. Вот полный список команд и возможностей, которые ты можешь использовать:

Основные команды:
/start
Начни взаимодействие с ботом. После ввода этой команды я покажу тебе основное меню, где ты сможешь выбрать интересующие тебя темы.

/help
Эта команда покажет тебе список всех доступных команд и функций. Ты всегда можешь обратиться сюда, если не уверен, как дальше использовать бота.

/about
Узнай больше о боте: кто его создал, какие цели он преследует и как работает. Это поможет тебе понять, для чего создан этот бот и как им пользоваться.

/menu
Возвращает тебя в главное меню, где ты можешь выбрать интересующие темы для получения актуальной информации.""")

@dp.message(F.text == 'Выбрать тему')
async def choose_theme(message:types.Message):
    keyboard = generate_menu_keyboard()
    await message.answer("Выберите тему", reply_markup=keyboard)

@dp.message(F.text == 'Новости')
async def news(message:types.Message):
    await message.answer('Сегодня: курс доллара вырос на 2%, акции падают.')

@dp.message(F.text == 'курсы валют')
async def news(message:types.Message):
    await message.answer('Доллар: 85₽, Евро: 90₽.')

@dp.message(F.text == '.Контактная информация')
async def news(message:types.Message):
    await message.answer('Наша почта: info@example.com. Телефон: +123456789..')

@dp.message(F.text == 'Часто задаваемые вопросы (FAQ)')
async def news(message:types.Message):
    await message.answer('Что делать, если бот не отвечает? - Убедись, что выбрал правильную тему.\n')


async def main():
    print("Запуск Бота")
    await dp.start_polling(bot)

asyncio.run(main())