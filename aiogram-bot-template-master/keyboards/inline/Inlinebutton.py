from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback, mentor_callback,Ict_callback  


course = {
"Web programming":"course_Web_programming",
"Mobil programming":"course_Mobil_programming",
"Desktop programming":"course_Desktop_programming",
"Computer graphics":"course_Computer_graphics",
"Computer science":"course_Computer_science",
"System Administration (Cisco)":"course_System_Administration_(Cisco)",


}

course_button = InlineKeyboardMarkup(row_width=2 )
for key,value in course.items() :
    python = InlineKeyboardButton(text=key, callback_data=course_callback.new(item_name=value))
    course_button.insert(python)   

mentor = {
"Web programming":"mentor_Web_programming",
"Mobil programming":"mentor_Mobil_programming",
"Desktop programming":"mentor_Desktop_programming",
"Computer graphics":"mentor_Computer_graphics",
"Computer science":"mentor_Computer_science",
"System Administration (Cisco)":"mentor_System_Administration_(Cisco)",


}

mentor_button = InlineKeyboardMarkup(row_width=2 )
for key,value in mentor.items() :
    mentor = InlineKeyboardButton(text=key, callback_data=mentor_callback.new(item_name=value))
    mentor_button.insert(mentor)  


Ict = {
'🔗 Ict Telegram sahifasi':'https://t.me/ictacademy_uz',
'🔗 Ict Instagram sahifasi':'https://instagram.com/ictacademy_uz',
'🔗 Ict Internet sayti':'http://ictacademy.uz/',
}

Ict_button = InlineKeyboardMarkup(row_width=2 )
for key,value in Ict.items() :
    Ict = InlineKeyboardButton(text=key, url=value)
    Ict_button.insert(Ict) 
