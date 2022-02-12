from aiogram import types
from keyboards.inline.Inlinebutton import course_button,mentor_button,Ict_button
from aiogram.types import CallbackQuery
from loader import dp


@dp.message_handler(text='📚 Kurslar')
async def course(message: types.Message):
    await message.answer('Siz 📚 Kurslar bo`limini tanladingiz.\nKurslardan birini tanlang.',reply_markup=course_button)

@dp.message_handler(text="🤵🏻 O`qituvchilar")
async def mentor(message: types.Message):
    await message.answer('Siz 🤵🏻 O`qituvchilar bo`limini tanladingiz.\nKurslardan birini tanlang.',reply_markup=mentor_button)

@dp.message_handler(text="📄 Ict haqida ma`lumot")
async def Ict_menu(message: types.Message):
    await message.answer('Siz 📄 Ict haqida ma`lumot bo`limini tanladingiz.\nTamoqlardan birini tanlang.',reply_markup=Ict_button)