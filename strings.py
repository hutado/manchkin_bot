#!/usr/bin/env python
# -*- coding: utf-8 -*-

NOT_AVAILABLE = '''
Это действие вам не доступно
Напишите админу бота: @hutado
'''

STANDART_STRING = '''
Возможно это действие здесь недоступно.
Перейдите в соответствующее меню.
Либо команда боту неизвестна.
'''

GAME_STRING = '''
*Ваш Уровень:* _{}_
*Ваша сила:*   _{}_
*Ваш пол:* _{}_
*Ваша раса:* {}
*Ваш класс:* {}
'''

# Строки с правилами
BASIC_RULES = '''
`ОСНОВНЫЕ ПРАВИЛА`:
1. Ничто не может опустить уровень манчкина ниже 1, хотя его боевая сила может быть нулевой и даже отрицательной.
2. Ты получаешь уровень после боя, только если *убил* монстра.
3. Ты не можешь получить награду за победу над монстром (сокровища, уровни) посреди боя. Выйграй бой прежде чем тянуть лапы к награде.
4. Ты можешь получить 10-й уровень *только* за убийство монстра.

`ПОДГОТОВКА К ИГРЕ`:
В начале игры твой манчкин - человек 1-го уровня без класса. Манчкины бывают мужского или женского пола. Изначально пол твоего манчкина совпадает с твоим собственным, если только ты не объявишь, что это не так.

Сдайте по две карты из каждой колоды всем игрокам (для быстрой игры по 4).

Изучи доставшиеся тебе 4 (8, если игра быстрая) карты. При желании можешь сыграть - выложить с руки на стол перед собой - по одной карте расы и класса и сколько угодно карт шмоток (если они не требуют от тебя чего-нибудь особенного).
'''

ALLOWED_ACTIONS = '''
*В любой момент игры ты можешь:*
- сбросить класс или расу
- сыграть карту _Получи уровень_
- сыграть _Ловушку_

*В любой момент игры, когда ты не в бою, ты можешь:*
- обменяться шмотками с другим игроком (он тоже должен быть не в бою)
- снять одни шмотки, надеть другие
- сыграть только что полученную карту (некоторые карты можно сыграть и в бою)

*Только в свой ход ты можешь:*
- сыграть новый класс или расу (в любой момент хода)
- продать шмотки за уровни (в любой момент, кроме боя)
- сыграть шмотку (большинство шмоток нельзя играть в бою, но некоторые разовые можно)
'''

PHASES = '''
В начале своего хода ты можешь играть карты, снимать и надевать шмотки, меняться шмотками с другими игроками и продавать шмотки за уровни. Когда сделаешь со своими картами все, что хотел, переходи к 1-й фазе.

*1. Вышибаем дверь!*
Вскрой верхнюю `дверь` из колоды. Если это _монстр_, ты должен с ним биться. Если ты вскрыл карту _ловушки_, она тут же действует на твоего манчкина (если может) и сбрасывается (или остается лежать перед тобой, если у нее длительный эффект). Если вышла любая другая карта, можешь тут же сыграть ее или взять в руку.

*2. Ищем неприятности или чистим нычки*
Если в фазе 1 ты встретил монстра, *пропусти* эту фазу
Если ты, выбив дверь, НЕ встретил монстра, у тебя на выбор 2 варианта:
`Ищи неприятности:` сыграй `с руки` карту монстра и подерись с ним по обычным правилам.
`Чисть нычки:` возьми вторую карту `двери` из колоды на руку, `не показывая соперникам`.

*3. От щедрот*
Если у тебя на руке больше *5* карт, _либо_ сыграй лишние карты, _либо_ отдай излишки персонажу с наименьшим уровнем. Если твой манчкин самый низкоуровневый (или один из таких), просто сбрось лишние карты.
'''

CLOTHES = '''
У каждой шмотки есть имя, сила и ценность в кредитах.
Шмоточная карта на твоей руке не идет в счет, пока ты не сыграл карту. В этот момент она становится `взятой` шмоткой. Ты можешь `взять` сколько угодно шмоток, но только один *Агрегат*.
`Взятая` шмотка не дает тебе бонусов, пока ты ее не `наденешь`.
Можно надеть только один `Головняк`, один `Броник`, одну пару `Обувки` и две `ручных` шмотки (или одну `двуручную`), если только у тебя нет карты или свойства, позволяющих носить больше.
Отмечай шмотки, которые не надел, поворачивая их боком.

В свой ход ты можешь скинуть шмотки на сумму в 1000 кредитов и немедленно получить один уровень. Можно обращать в уровни как взятые шмотки, так и шмотки из руки.

Продавать, менять или красть шмотки во время боя или при смывке нельзя.
'''

TEAM = '''
Ты можешь сыграть `Напарника` в любой момент, даже в бою, пока у тебя в игре не более одного `Напарника` одновременно (два для `Купца`).
Ты можешь сбросить `Напарника` в любой момент.

`Напарник` может пожертвовать собой ради твоего спасения.
Если ты проиграл бой, вместо броска на смывку можешь сбросить `Напарника` вместе со всем, что он нес.
Так ты автоматически смываешься от всех монстров в этом бою, даже если карта монстра гласит, что смывка невозможна.
Если кто-то помогал тебе в бою, *ТЫ* решаешь, смоется ли и твой помощник автоматически, или будет бросать кубик на смывку.
'''

MOMENTS = '''
Некоторые свойства требуют от тебя сбросить карты. Если нет указания, откуда именно надо сбрасывать, то их можно сбрасывать как с руки, так и из игры.

Сбросить класс или расу можно в любой момент игры, даже в бою.

Карты `Суперманчкин` и `Полукровка` нельзя играть, если не принадлежишь ни к одному классу или ни к одной расе.

Все усилители монстров складываются между собой, и все, что усиливает монстра, усиливает и его `клона`.
Однако если в игре уже присутствуют два монстра, один из которых вошел в игру по карте `Бродячей твари`, игрок, применивший усилитель, должен выбрать, какого монстра он усиливает.

Если ты помогаешь кому-либо или дерешься вне очереди по какой-то другой причине, ты не можешь выводить новые шмотки из руки на стол.

Если `Ловушка` может поразить больше одной шмотки, жертва решает, какие шмотки потеряны или изменены.

Комбинированное оружие (`Лазеры`) можно разбирать и считать каждую карту 1 шмоткой. Нельзя подвергнуть все оружие целиком `Аннигиляции` или `Антиматерии`, только 1 карту.

Если ты победил монстра, не убив его, твой уровень не увеличивается.
'''

DEATH = '''
Если ты умер, ты теряешь все имущество. Остаются только `Класс`, `Раса` и `Уровень`.

*Мародерство*: положите карты с руки рядом с теми, что у тебя в игре. Начиная с самого высокоуровнего героя, другие игроки по очереди выбирают себе по одной карте.
После того, как все получили по одной карте, остатки сбрасываются.

На следующем твоем ходу возьми в темную по две карты из каждой колоды, как в начале игры.
'''

CHANGING = '''
Ты можешь обмениваться с другими игроками `Шмотками` (но не другими картами).
Меняться можно только шмотками со стола, но не из руки.
Можно отдавать шмотки для подкупа других игроков.

Меняйся в любой момент игры, за исключением боя. Любая шмотка, которую ты получил, выходит на стол. Продать ее нельзя до твоего следующего хода.
'''
