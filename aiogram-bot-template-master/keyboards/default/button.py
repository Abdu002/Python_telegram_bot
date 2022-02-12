from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📚 Kurslar'),
            KeyboardButton(text="🤵🏻 O`qituvchilar"),
        ],
        [
            KeyboardButton(text='📄 Ict haqida ma`lumot'),
        ],
    ],
    resize_keyboard=True
)