import aiogram.utils.markdown as fmt
import src.keyboards.keyboards as kb

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from src.dtb.dtb import *

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Добро пожаловать в чат-бота!", reply_markup=kb.main)
    try:
        cursor.execute(f"SELECT uid FROM users WHERE uid = '{message.from_user.id}'")
        if not cursor.fetchone() is None:
            pass
        else:
            info = (f"INSERT INTO users (uid,name) VALUES(%s, %s)")
            infoinsert = (f'{message.from_user.id}', f'{message.from_user.username}')
            cursor.execute(info, infoinsert)
            connection.commit()
    except Exception as ext:
        print(ext)



@router.message(F.text == 'Профиль')
async def profile(message: Message):
    cursor.execute(f"SELECT name FROM users WHERE uid = {message.from_user.id}")
    name = cursor.fetchone()
    cursor.execute(f"SELECT id FROM users WHERE uid = {message.from_user.id}")
    id = cursor.fetchone()
    await message.answer(
        fmt.text(
            fmt.text("🖥 Ваш профиль:"),
            fmt.text("├ Имя:", fmt.hbold(f"{name[0]}")),
            fmt.text("└ Id:", fmt.hbold(f"{id[0]}")),
            sep="\n"
        ), parse_mode="HTML"
    )


@router.message(F.text == 'Справка')
async def spravka(message: Message):
    await message.answer(
        fmt.text(
            fmt.text("💖 Здесь живёт красота"),
            fmt.text(),
            fmt.text(fmt.hbold("Усадьба Курлиных"), "– это целостная архитектурно-историческая среда, культурная модель эпохи конца XIX - начала XX веков, времени наивысшего расцвета купеческой Самары."),
            fmt.text("Усадьбу Курлиных по праву называют ", fmt.hbold("«жемчужиной»") , "самарской архитектуры. Музей открылся в конце 2012 года, он занимается изучением истории владельцев особняка, сбором информации и предметов той эпохи."),
            fmt.text(),
            fmt.text("📢 Время работы:"),
            fmt.text(fmt.hbold("Понедельник – выходной")),
            fmt.text("Вторник – ",fmt.hunderline("10:00 - 18:00")),
            fmt.text("Среда – ",fmt.hunderline("10:00 - 18:00")),
            fmt.text("Четверг – ",fmt.hunderline("13:00 - 21:00")),
            fmt.text("Пятница – ",fmt.hunderline("10:00 - 18:00")),
            fmt.text("Суббота – ",fmt.hunderline("10:00 - 18:00")),
            fmt.text("Воскресенье – ",fmt.hunderline("10:00 - 18:00")),
            fmt.text(),
            fmt.text("🚆 Адрес:"),
            fmt.text("Город Самара ,Ул. ", fmt.hunderline("Фрунзе 159") ),
            sep="\n"
        ), parse_mode="HTML"
    )


@router.message(F.text == 'Как добраться')
async def catalog(message: Message):
    latitude = 53.19422074304731
    longitude = 50.09629657777664
    await message.answer_location(latitude=latitude, longitude=longitude)
    await message.answer(
        fmt.text(
            fmt.text(),
            fmt.text("🚆 Адрес:"),
            fmt.text("Город Самара ,Ул. ", fmt.hunderline("Фрунзе 159")),
            sep="\n"
        ), parse_mode="HTML"
    )

@router.message(F.text == 'Покупка Билетов')
async def vistavki(message: Message):
    await message.answer_photo(photo="https://i.imgur.com/iGaGR2L.png")
    await message.answer_photo(photo="https://i.imgur.com/HIFrTFE.png")
    await message.answer_photo(photo="https://i.imgur.com/RNcWMkQ.png")

@router.message(F.text == 'Выставки')
async def vistavki(message: Message):
    await message.answer('Здесь представленные основные экспозиции музея', reply_markup=kb.catalog)


@router.callback_query(F.data == 'Новый символизм')
async def simvol(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://i.imgur.com/fDWoFuF.jpeg")
    await callback.message.answer(
        fmt.text(
            fmt.text("Гиперборея и киберпространство"),
            fmt.text(),
            fmt.text(fmt.hbold("Новый символизм"),
                     "– Галерея Виктория вместе с Музеем Модерна представляет выставку «Новый символизм: Гиперборея и киберпространство», посвященную символистской поэтике в современном искусстве."),
            fmt.text(),
            sep="\n"
        ), parse_mode="HTML"
    )

@router.callback_query(F.data == 'Бремя Модерна')
async def bremya(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://i.imgur.com/qUUE5Li.jpeg")
    await callback.message.answer(
        fmt.text(
            fmt.text("Человек определяет место или место определяет человека?"),
            fmt.text(),
            fmt.text(fmt.hbold("Бремя Модерна"),
                     " - Выставка «Бремя модерна» является исследованием жизни обычных людей в домах, построенных в начале ХХ века в стиле модерн"),
            fmt.text(),
            sep="\n"
        ), parse_mode="HTML"
    )

@router.callback_query(F.data == 'Любовные Сцены')
async def sex(callback: CallbackQuery):
    await callback.message.answer_photo(photo="https://i.imgur.com/hTYs5LO.jpeg")
    await callback.message.answer(
        fmt.text(
            fmt.text("Выставочный проект в основной экспозиции Музея Модерна"),
            fmt.text(),
            fmt.text(fmt.hbold("Любовные Сцены"),
                     "- Наш выставочный проект посвящён одному из самых сильных чувств человека – любви. Цикл состоит из 4 выставок, которые будут меняться в течение года и обозначать этапы любовных отношений."),
            fmt.text(),
            sep="\n"
        ), parse_mode="HTML"
    )


