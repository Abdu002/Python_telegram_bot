from aiogram import types
from keyboards.inline.callback_data import course_callback,  mentor_callback, Ict_callback
from keyboards.inline.Inlinebutton import course_button
from keyboards.inline.web_kurslar import w_mavzu
from keyboards.inline.Mobile import m_mavzu
from keyboards.inline.Desktop import d_mavzu
from keyboards.inline.Computer_graphics import g_mavzu
from keyboards.inline.Computer_science import s_mavzu
from keyboards.inline.sistem import a_mavzu
from aiogram.types import CallbackQuery
from loader import dp


@dp.callback_query_handler(course_callback.filter(item_name='course_Web_programming'))
async def course_web(call:CallbackQuery):
    await call.message.answer('Siz Web programming bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=w_mavzu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(course_callback.filter(item_name='course_Mobil_programming'))
async def course_mobile(call:CallbackQuery):
    await call.message.answer('Siz Mobil programming bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=m_mavzu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(course_callback.filter(item_name='course_Desktop_programming'))
async def course_desktop(call:CallbackQuery):
    await call.message.answer('Siz Desktop programming bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=d_mavzu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(course_callback.filter(item_name='course_Computer_graphics'))
async def course_graphics(call:CallbackQuery):
    await call.message.answer('Siz Computer graphics bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=g_mavzu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(course_callback.filter(item_name='course_Computer_science'))
async def course_science(call:CallbackQuery):
    await call.message.answer('Siz Computer science bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=s_mavzu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(course_callback.filter(item_name='course_System_Administration_(Cisco)'))
async def course_sistem(call:CallbackQuery):
    await call.message.answer('Siz Computer science bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=a_mavzu)
    await call.message.delete()
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=course_button)
    await call.answer()




