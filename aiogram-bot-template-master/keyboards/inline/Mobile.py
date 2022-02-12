from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_mobile_mavzu 

mobile_programming_mavzu = {
"Android ( JAVA)":"m_course_Android",
"Flutter":"m_course_Flutter",
}

m_mavzu = InlineKeyboardMarkup(row_width=2)
for key,value in mobile_programming_mavzu.items() :
    python = InlineKeyboardButton(text=key, callback_data=course_mobile_mavzu.new(item_name=value))
    m_mavzu.insert(python)  

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
m_mavzu.insert(back_button)