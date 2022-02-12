# from aiogram import types
# from keyboards.inline.callback_data import course_callback, course_mentor_mavzu, course_python_mavzu, mentor_callback, Ict_callback
# from keyboards.inline.mentor_kurslar import m_mavzu
# from aiogram.types import CallbackQuery
# from loader import dp

# @dp.callback_query_handler(mentor_callback.filter(item_name="mentor_Python"))
# async def course_Python(call:CallbackQuery):
#     await call.message.answer('Siz Python o`qituvchisi bo`limini tanladingiz.\nO`qituvchilardan birini tanlang.',reply_markup=m_mavzu)
#     await call.message.delete()
#     await call.answer(cache_time=60)