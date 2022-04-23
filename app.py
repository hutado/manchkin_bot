#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from aiogram import types
from aiogram.utils.executor import start_webhook

import db
import config
import strings
import keyboard


async def on_startup(dispatcher):
    await db.create_table()
    await config.bot.set_webhook(config.WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await config.bot.delete_webhook()


###################
# Handle commands #
###################

@config.dp.callback_query_handler()
@db.check_rights
async def callback_inline(call: types.CallbackQuery):
    """Обработка inline-кнопок"""

    user_id = call.message.chat.id
    config.bot.answer_callback_query(call.id)
    info = ''
    _keyboard = keyboard.inline_keyboard()

    # Кнопка Человек
    if call.data == "human":
        await db.change_race(user_id, "Человек")

    # Кнопка Котейка
    if call.data == "cat":
        await db.change_race(user_id, "Котейка")

    # Кнопка Купец
    if call.data == "seller":
        await db.change_race(user_id, "Купец")

    # Кнопка Сенс
    if call.data == "sens":
        await db.change_race(user_id, "Сенс")

    # Кнопка Киборг
    if call.data == "cyborg":
        await db.change_class(user_id, "Киборг")

    # Кнопка Мутант
    if call.data == "mutant":
        await db.change_class(user_id, "Мутант")

    # Кнопка Голохотник
    if call.data == "hunter":
        await db.change_class(user_id, "Голохотник")

    # Кнопка Гаджестянщик
    if call.data == "scientist":
        await db.change_class(user_id, "Гаджестянщик")

    # Кнопка Без класса
    if call.data == "without":
        await db.change_class(user_id, "Без класса")

    # Кнопка Доступные действия
    if call.data == "actions":
        info = strings.ALLOWED_ACTIONS
        _keyboard = keyboard.rules_keyboard()

    # Кнопка Фазы
    if call.data == "phases":
        info = strings.PHASES
        _keyboard = keyboard.rules_keyboard()

    # Кнопка Шмотки
    if call.data == "clothes":
        info = strings.CLOTHES
        _keyboard = keyboard.rules_keyboard()

    # Кнопка Спорные моменты
    if call.data == "moments":
        info = strings.MOMENTS
        _keyboard = keyboard.rules_keyboard()

    # Кнопка Напарники
    if call.data == "team":
        info = strings.TEAM
        _keyboard = keyboard.rules_keyboard()

    # Кнопка Обмен
    if call.data == "changing":
        info = strings.CHANGING
        _keyboard = keyboard.rules_keyboard()

    # Кнопка Смерть
    if call.data == "death":
        info = strings.DEATH
        _keyboard = keyboard.rules_keyboard()

    info = info or await db.select_info(user_id)

    return await config.bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=info,
        parse_mode='Markdown',
        reply_markup=_keyboard
    )


@config.dp.message_handler(commands=['start'])
@db.check_rights
async def start(message: types.Message):
    """/start handler"""

    await db.add_user(message.chat.id, message.chat.username or message.chat.first_name)
    info = await db.select_info(message.chat.id)

    return await message.answer(info, parse_mode='Markdown', reply_markup=keyboard.keyboard_game())


###################
#  Manchkin menu  #
###################

@config.dp.message_handler(regexp=config.BUTTON['rules'])
@db.check_rights
async def show_rules(message: types.Message):
    """Обработка нажатия кнопки Правила"""

    return await message.answer(strings.BASIC_RULES, parse_mode='Markdown', reply_markup=keyboard.rules_keyboard())


@config.dp.message_handler(regexp=config.BUTTON['reload'])
@db.check_rights
async def reload_info(message: types.Message):
    """Обработка нажатия кнопки Обновить"""

    info = await db.select_info(message.chat.id)

    return await message.answer(info, parse_mode='Markdown', reply_markup=keyboard.inline_keyboard())


@config.dp.message_handler(regexp=config.BUTTON['str_up'])
@db.check_rights
async def strength_up(message: types.Message):
    """Обработка нажатия кнопки Увеличить силу"""

    await db.strength_change(message.chat.id, 1)
    info = await db.select_info(message.chat.id)

    return await message.answer(info, parse_mode='Markdown', reply_markup=keyboard.inline_keyboard())


@config.dp.message_handler(regexp=config.BUTTON['str_down'])
@db.check_rights
async def strength_down(message: types.Message):
    """Обработка нажатия кнопки Уменьшить силу"""

    await db.strength_change(message.chat.id, -1)
    info = await db.select_info(message.chat.id)

    return await message.answer(info, parse_mode='Markdown', reply_markup=keyboard.inline_keyboard())


@config.dp.message_handler(regexp=config.BUTTON['lvl_up'])
@db.check_rights
async def lvl_up(message: types.Message):
    """Обработка нажатия кнопки Повысить уровень"""

    await db.lvl_change(message.chat.id, 1)
    info = await db.select_info(message.chat.id)

    return await message.answer(info, parse_mode='Markdown', reply_markup=keyboard.inline_keyboard())


@config.dp.message_handler(regexp=config.BUTTON['lvl_down'])
@db.check_rights
async def lvl_down(message: types.Message):
    """Обработка нажатия кнопки Понизить уровень"""

    await db.lvl_change(message.chat.id, -1)
    info = await db.select_info(message.chat.id)

    return await message.answer(info, parse_mode='Markdown', reply_markup=keyboard.inline_keyboard())


@config.dp.message_handler(regexp=config.BUTTON['lvl_drop'])
@db.check_rights
async def lvl_dropdown(message: types.Message):
    """Обработка нажатия кнопки Сбросить уровень"""

    await db.lvl_dropdown(message.chat.id)
    info = await db.select_info(message.chat.id)

    return await message.answer(info, parse_mode='Markdown', reply_markup=keyboard.inline_keyboard())


@config.dp.message_handler(regexp=config.BUTTON['sex'])
@db.check_rights
async def change_sex(message: types.Message):
    """Обработка нажатия кнопки Поменять пол"""

    await db.change_sex(message.chat.id)
    info = await db.select_info(message.chat.id)

    return await message.answer(info, parse_mode='Markdown', reply_markup=keyboard.inline_keyboard())


@config.dp.message_handler(regexp=config.BUTTON['race'])
@db.check_rights
async def change_race(message: types.Message):
    """Изменить расу"""

    return await message.answer('Выберите расу:', parse_mode='Markdown', reply_markup=keyboard.race_keyboard())


@config.dp.message_handler(regexp=config.BUTTON['class'])
@db.check_rights
async def change_class(message: types.Message):
    """Изменить класс"""

    return await message.answer('Выберите класс:', parse_mode='Markdown', reply_markup=keyboard.class_keyboard())


@config.dp.message_handler(content_types=["text"])
@db.check_rights
async def standart_message(message: types.Message):
    """Обработка остальных команд"""

    if message.chat.id == config.ADMIN:
        if message.text.startswith('add'):
            user_id = message.text.replace('add', '').strip()
            await message.answer(f'Добавляем пользователя {user_id} в белый список')

            return await db.add_to_whitelist(int(user_id))

    # Прибавление и убавление силы из чата
    if message.text.startswith('+') or message.text.startswith('-'):
        try:
            changes = int(message.text)
            db.strength_change(message.chat.id, changes)
        except ValueError:
            await message.answer(f'После + должно быть число')

        info = await db.select_info(message.chat.id)

        return await message.answer(info, parse_mode='Markdown', reply_markup=keyboard.inline_keyboard())

    return await message.answer(strings.STANDART_STRING, parse_mode='Markdown', reply_markup=keyboard.keyboard_game())


###################
# Starting Server #
###################

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=config.dp,
        webhook_path=config.WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT,
    )
