#!/usr/bin/env python
# -*- coding: utf-8 -*-

from databases import Database

import config
import strings


database = Database(config.DB_URL)


async def create_table():
    """Создание таблицы"""

    sql_users = """
        CREATE TABLE IF NOT EXISTS "Users" (
            "UserID" INTEGER NOT NULL PRIMARY KEY,
            "Nickname" TEXT NOT NULL,
            "Level" INTEGER NOT NULL DEFAULT 1 CHECK ("Level" > 0 AND "Level" <= 10),
            "Sex" BOOLEAN NOT NULL DEFAULT TRUE,
            "Strength" INTEGER NOT NULL DEFAULT 0,
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

    async def wrapper(message):
        sql = """
            SELECT
                "UserID"
            FROM
                "WhiteList"
            WHERE
                "UserID" = :user_id
        """

        if 'chat' in message:
            user_id = message.chat.id
        else:
            user_id = message.message.chat.id

        if await database.fetch_one(sql, values={'user_id': user_id}):
            return await func(message)
        return await message.answer(strings.NOT_AVAILABLE)

    return wrapper


async def add_to_whitelist(user_id):
    """Добавление в белый список"""

    sql = """
        INSERT INTO
            "WhiteList" (
                "UserID"
            )
        VALUES (
            :user_id
        )
        ON CONFLICT DO NOTHING
    """

    await database.execute(sql, values={'user_id': user_id})


async def select_info(user_id):
    """Получение данных о пользователе"""

    sql = """
        SELECT
            "Level"
            , "Sex"
            , "Strength"
            , "Race"
            , "Class"
        FROM
            "Users"
        WHERE
            "UserID" = :user_id
    """

    sql_opp = """
        SELECT
            "Nickname"
            , "Level"
            , "Sex"
            , "Strength"
            , "Race"
            , "Class"
        FROM
            "Users"
        WHERE
            "UserID" <> :user_id
    """

    user_info = await database.fetch_one(sql, values={'user_id': user_id})
    opp_info = await database.fetch_all(sql_opp, values={'user_id': user_id})

    lvl = user_info[0]
    sex = 'Мужчина' if user_info[1] else 'Женщина'
    strength = user_info[2] + lvl
    race = user_info[3]
    class_ = user_info[4]
    string = strings.GAME_STRING.format(config.LVLS[lvl], strength, sex, config.EMOJI[race] + race, config.EMOJI[class_] + class_)

    for row in opp_info:
        opp_sex = 'Мужчина' if row[2] else 'Женщина'
        string = f'{string}\n*{row[0]}*\n`Уровень:` {config.LVLS[row[1]]}\n`Сила:` {row[3] + row[1]}\n`Пол:` {opp_sex}\n`Раса:` {config.EMOJI[row[4]] + row[4]}\n`Класс:` {config.EMOJI[row[5]] + row[5]}\n'

    return string


async def lvl_change(user_id, lvl):
    """Изменение уровня"""

    sql = """
        BEGIN;
        SAVEPOINT lvl_savepoint;
        UPDATE
            "Users"
        SET
            "Level" = "Level" + :lvl
        WHERE
            "UserID" = :user_id;
        ROLLBACK TO SAVEPOINT lvl_savepoint;
        COMMIT;
    """

    await database.execute(sql, values={'user_id': user_id, 'lvl': lvl})


async def lvl_dropdown(user_id):
    """Сброс персонажа"""

    sql = """
        UPDATE
            "Users"
        SET
            "Level" = 1
            , "Strength" = 0
            , "Sex" = TRUE
            , "Race" = 'Человек'
            , "Class" = 'Без класса'
        WHERE
            "UserID" = :user_id
    """

    await database.execute(sql, values={'user_id': user_id})


async def change_sex(user_id):
    """Смена пола"""

    sql = """
        UPDATE
            "Users"
        SET
            "Sex" = NOT "Sex"
        WHERE
            "UserID" = :user_id
    """

    await database.execute(sql, values={'user_id': user_id})


async def strength_change(user_id, changes):
    """Изменение силы"""

    sql = """
        UPDATE
            "Users"
        SET
            "Strength" = "Strength" + :strength
        WHERE
            "UserID" = :user_id
    """

    await database.execute(sql, values={'user_id': user_id, 'strength': changes})


async def change_race(user_id, race):
    """Изменение расы"""

    sql = """
        UPDATE
            "Users"
        SET
            "Race" = :race
        WHERE
            "UserID" = :user_id
    """

    await database.execute(sql, values={'user_id': user_id, 'race': race})


async def change_class(user_id, class_):
    """Изменение расы"""

    sql = """
        UPDATE
            "Users"
        SET
            "Class" = :class
        WHERE
            "UserID" = :user_id
    """

    await database.execute(sql, values={'user_id': user_id, 'class': class_})
