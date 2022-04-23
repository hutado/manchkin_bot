#!/usr/bin/env python
# -*- coding: utf-8 -*-

from databases import Database

from config import DB_URL


database = Database(DB_URL)


async def create_table():
    """Создание таблицы"""

    sql = """
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

    await database.connect()
    await database.execute(sql)


async def add_user(user_id):
    """Добавление пользователя"""

    sql = """
        INSERT INTO
            "Users" (
                "UserID"
            )
        VALUES (
            :user_id
        )
        ON CONFLICT DO NOTHING
    """

    await database.execute(sql, values={'user_id': user_id})


async def read():
    sql = """
        SELECT * FROM "Users"
    """

    users = await database.fetch_all(sql)

    return users
