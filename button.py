from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

MENU = ['Новости', "курсы валют", ".Контактная информация", "Часто задаваемые вопросы (FAQ)"]

keydord_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Выбрать тему")],
    ],
    resize_keyboard=True
)

def generate_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=menu)] for menu in MENU ],
        resize_keyboard=True
    )

