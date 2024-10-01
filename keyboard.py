from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/Регистрация'), KeyboardButton(text='Наш сайт')],
        [KeyboardButton(text='/Game')]
    ],
    resize_keyboard=True
)
urls = InlineKeyboardMarkup(inline_keyboard= 
[
    [InlineKeyboardButton(text='Сайт', url='Salat21345.pythonanywhere.com')]
])

