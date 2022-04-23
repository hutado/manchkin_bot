#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from aiogram import types
from aiogram.utils.executor import start_webhook

import db
import config
import keyboard
from strings import STANDART_STRING


async def on_startup(dispatcher):
    await db.create_table()
    await config.bot.set_webhook(config.WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await config.bot.delete_webhook()


@config.dp.message_handler(commands=['start'])
@db.check_rights
async def start(message: types.Message):
    """/start handler"""

    await db.add_user(message.chat.id, message.chat.username or message.chat.first_name)
    info = await db.select_info(message.chat.id)
    return await message.answer(info, parse_mode='Markdown', reply_markup=keyboard.keyboard_game())


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

    return await message.answer(STANDART_STRING, parse_mode='Markdown', reply_markup=keyboard.keyboard_game())


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
