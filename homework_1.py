# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# import random
# from config import token

# bot = Bot(token=token)
# dp = Dispatcher()

# @dp.message(Command("start"))
# async def start_game(message: types.Message):
#     """Обработка команды /start"""
#     await message.answer("Давайте сыграем в 'Камень, ножницы, бумага' Напишите свой выбор: Камень, Ножницы или Бумага")

# @dp.message()
# async def handle_rps(message: types.Message):
#     """Обработка выбора игрока"""
#     user_choice = message.text.lower()
#     bot_choice = random.choice(["камень", "ножницы", "бумага"])

#     # Определение результата
#     result = ""
#     if user_choice == bot_choice:
#         result = "Ничья!"
#     elif (user_choice == "камень" and bot_choice == "ножницы") or \
#          (user_choice == "ножницы" and bot_choice == "бумага") or \
#          (user_choice == "бумага" and bot_choice == "камень"):
#         result = "Вы выиграли!"
#     elif user_choice in ["камень", "ножницы", "бумага"]:
#         result = "Вы проиграли!"
#     else:
#         await message.answer("Неправильный выбор. Пожалуйста, напишите: Камень, Ножницы или Бумага.")
#         return

#     # Ответ игроку
#     await message.answer(
#         f"Вы выбрали: {user_choice.capitalize()}\nБот выбрал: {bot_choice.capitalize()}\n\n{result}"
#     )

# if __name__ == "__main__":
#     dp.run_polling(bot)