#!/usr/bin/env python
# -*- coding: utf-8 -*-

from databases import Database


database = Database('sqlite:///bot.db')


async def create_table():
    """
    Создание таблицы
    """

    sql = """
        CREATE TABLE IF NOT EXISTS "Users" (
            "UserID" INTEGER NOT NULL PRIMARY KEY,
            "Nickname" TEXT NOT NULL,
            "Level" INTEGER NOT NULL DEFAULT 1,
            "Sex" INTEGER NOT NULL DEFAULT 0,
            "Strength" INTEGER NOT NULL DEFAULT 1,
            "Race" TEXT NOT NULL DEFAULT "Человек",
            "Class" TEXT NOT NULL DEFAULT "Без класса"
        )
    """

    await database.execute(sql)


async def read():
    sql = """
        SELECT * FROM "Users"
    """

    users = await database.fetch_all(sql)

    return users
