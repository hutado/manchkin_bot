#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from config import BUTTON


def keyboard_game():
    """Основная клавиатура"""

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(BUTTON['lvl_up'], BUTTON['lvl_down'])
    markup.row(BUTTON['str_up'], BUTTON['str_down'])
    markup.row(BUTTON['lvl_drop'], BUTTON['sex'])
    markup.row(BUTTON['race'], BUTTON['class'])
    markup.row(BUTTON['reload'], BUTTON['rules'])

    return markup


def inline_keyboard():
    """Inline кнопка Обновить"""

    markup = InlineKeyboardMarkup()
    reload_button = InlineKeyboardButton(text="Обновить", callback_data="reload")
    markup.add(reload_button)

    return markup


def rules_keyboard():
    """Клавиатура правил"""

    markup = InlineKeyboardMarkup()
    actions = InlineKeyboardButton(text="Доступные действия", callback_data="actions")
    phases = InlineKeyboardButton(text="Фазы", callback_data="phases")
    clothes = InlineKeyboardButton(text="Шмотки", callback_data="clothes")
    team = InlineKeyboardButton(text="Напарники", callback_data="team")
    changing = InlineKeyboardButton(text="Обмен", callback_data="changing")
    death = InlineKeyboardButton(text="Смерть", callback_data="death")
    moments = InlineKeyboardButton(text="Спорные моменты", callback_data="moments")

    markup.add(actions, phases)
    markup.add(clothes, team)
    markup.add(changing, death)
    markup.add(moments)

    return markup


def race_keyboard():
    """Клавиатура выбора расы"""

    markup = InlineKeyboardMarkup()
    human = InlineKeyboardButton(text="Человек", callback_data="human")
    cat = InlineKeyboardButton(text="Котейка", callback_data="cat")
    seller = InlineKeyboardButton(text="Купец", callback_data="seller")
    sens = InlineKeyboardButton(text="Сенс", callback_data="sens")

    markup.add(human, cat)
    markup.add(seller, sens)

    return markup


def class_keyboard():
    """Клавиатура выбора класса"""

    markup = InlineKeyboardMarkup()
    cyborg = InlineKeyboardButton(text="Киборг", callback_data="cyborg")
    mutant = InlineKeyboardButton(text="Мутант", callback_data="mutant")
    hunter = InlineKeyboardButton(text="Голохотник", callback_data="hunter")
    scientist = InlineKeyboardButton(text="Гаджестянщик", callback_data="scientist")
    without = InlineKeyboardButton(text="Без класса", callback_data="without")

    markup.add(cyborg, mutant)
    markup.add(hunter, scientist)
    markup.add(without)

    return markup
