#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from aiogram import types
from aiogram.utils.executor import start_webhook

import db
import config


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
    users = await db.read(message.chat.id)
    await message.answer(users)


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
