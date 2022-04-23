#!/usr/bin/env python
# -*- coding: utf-8 -*-

from databases import Database

from config import DB_URL
from strings import NOT_AVAILABLE


database = Database(DB_URL)


async def create_table():
    """Создание таблицы"""

    sql_users = """
        CREATE TABLE IF NOT EXISTS "Users" (
            "UserID" INTEGER NOT NULL PRIMARY KEY,
            "Nickname" TEXT NOT NULL,
            "Level" INTEGER NOT NULL DEFAULT 1,
            "Sex" INTEGER NOT NULL DEFAULT 0,
            "Strength" INTEGER NOT NULL DEFAULT 1,
            "Race" TEXT NOT NULL DEFAULT 'Человек',
            "Class" TEXT NOT NULL DEFAULT 'Без класса',
            CONSTRAINT "UserID_unique" UNIQUE ("UserID")
        );
    """

    sql_whitelist = """
        CREATE TABLE IF NOT EXISTS "WhiteList" (
            "UserID" INTEGER NOT NULL PRIMARY KEY,
            CONSTRAINT "UserID_whitelist_unique" UNIQUE ("UserID")
        );
    """

    await database.connect()
    await database.execute(sql_users)
    await database.execute(sql_whitelist)


async def add_user(user_id, nickname):
    """Добавление пользователя"""

    sql = """
        INSERT INTO
            "Users" (
                "UserID"
                , "Nickname"
            )
        VALUES (
            :user_id
            , :nickname
        )
        ON CONFLICT DO NOTHING
    """

    await database.execute(sql, values={'user_id': user_id, 'nickname': nickname})


def check_rights(func):
    """Проверка прав"""

    def wrapper(message):
        sql = """
            SELECT
                TRUE
            FROM
                "WhiteList"
            WHERE
                "UserID" = :user_id
        """

        if database.execute(sql, values={'user_id': message.chat.id}):
            return func(message)
        return message.answer(NOT_AVAILABLE)



    return wrapper
