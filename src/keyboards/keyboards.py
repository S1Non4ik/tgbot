from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Профиль')],
    [KeyboardButton(text='Справка')],
    [KeyboardButton(text='Как добраться')],
    [KeyboardButton(text='Покупка Билетов')],
    [KeyboardButton(text='Выставки')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Новый символизм', callback_data='Новый символизм')],
    [InlineKeyboardButton(text='Бремя Модерна', callback_data='Бремя Модерна')],
    [InlineKeyboardButton(text='Любовные Сцены', callback_data='Любовные Сцены')]])

