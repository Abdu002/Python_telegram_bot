from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_web_mavzu 

Web_programming_mavzu = {
"Frontend ":"w_course_Frontend",
"Backend ":"w_course_Backend",
"Framework ":"w_course_Framework",

}

w_mavzu = InlineKeyboardMarkup(row_width=2)
for key,value in Web_programming_mavzu.items() :
    python = InlineKeyboardButton(text=key, callback_data=course_web_mavzu.new(item_name=value))
    w_mavzu.insert(python)  

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
w_mavzu.insert(back_button)