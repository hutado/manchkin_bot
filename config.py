#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher


ADMIN = int(os.getenv('ADMIN_ID'))

# Настройки бота
TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# Настройки вебхуков
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# Настройки сервера
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

# Настройки БД
DB_URL = os.getenv('DATABASE_URL')

# Unicode-коды emoji
EMOJI = {
    'lvl_up': u'\U00002B06',
    'lvl_down': u'\U00002B07',
    'lvl_drop': u'\U00002B55',
    'rules': u'\U0001F4C4',
    'sex': u'\U0001F6BB',
    'str_up': u'\U000023EB',
    'str_down': u'\U000023EC',
    'reload': u'\U0001F504',
    'race': u'\U0001F468',
    'class': u'\U0001F9D9',
    'Котейка': u'\U0001F63E',
    'Купец': u'\U0001F473',
    'Сенс': u'\U0001F647',
    'Киборг': u'\U0001F916',
    'Мутант': u'\U0001F9DF',
    'Голохотник': u'\U0001F9B9',
    'Гаджестянщик': u'\U0001F468' + u'\U0000200D' + u'\U0001F52C',
    'Без класса': '',
    'Человек': u'\U0001F468',

}

# Кнопки
BUTTON = {
    'lvl_up': EMOJI['lvl_up'] + 'Поднять уровень',
    'lvl_down': EMOJI['lvl_down'] + 'Понизить уровень',
    'lvl_drop': EMOJI['lvl_drop'] + 'Сбросить персонажа',
    'rules': EMOJI['rules'] + 'Правила',
    'sex': EMOJI['sex'] + 'Сменить пол',
    'str_up': EMOJI['str_up'] + 'Увеличить силу',
    'str_down': EMOJI['str_down'] + 'Уменьшить силу',
    'reload': EMOJI['reload'] + 'Обновить',
    'race': EMOJI['race'] + 'Раса',
    'class': EMOJI['class'] + 'Класс',
}

# Иконки уровней
LVLS = {
    10: u'\U0001F51F',
    9: u'\U00000039'+ u'\U000020E3',
    8: u'\U00000038'+ u'\U000020E3',
    7: u'\U00000037'+ u'\U000020E3',
    6: u'\U00000036'+ u'\U000020E3',
    5: u'\U00000035'+ u'\U000020E3',
    4: u'\U00000034'+ u'\U000020E3',
    3: u'\U00000033'+ u'\U000020E3',
    2: u'\U00000032'+ u'\U000020E3',
    1: u'\U00000031'+ u'\U000020E3',
}
