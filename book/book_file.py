import os
import sys
import re
import sqlite3 as sq

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

DB_PATH = 'new.db'


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    substring = text[start:]

    # Находим позицию первого знака препинания из списка
    match = re.search(r'[,.!:;?]', substring)

    # Если нашли знак препинания
    if match:
        end = match.end()
    else:
        # Если знака препинания нет, берем всю оставшуюся часть текста
        end = len(substring)

    # Обрезаем текст по найденной позиции
    part_text = substring[:end]

    # Возвращаем текст страницы и его размер
    return part_text, len(part_text)


# Функция, создающая таблицу в базе данных
def create_table():
    connection = sq.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book_pages (
            page_number INTEGER PRIMARY KEY,
            page_text TEXT
        )
    ''')

    connection.commit()
    connection.close()


# Функция, формирующая записи в базе данных
def prepare_book(path: str):
    create_table()

    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    connection = sq.connect(DB_PATH)
    cursor = connection.cursor()

    start = 0
    page_number = 1

    while start < len(content):
        part_text, part_size = _get_part_text(content, start, PAGE_SIZE)
        cursor.execute('''
            INSERT INTO book_pages (page_number, page_text)
            VALUES (?, ?)
        ''', (page_number, part_text.lstrip()))

        start += part_size
        page_number += 1

    connection.commit()
    connection.close()


# # Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
# В этом коде используется база данных SQLite(book_pages.db).Функция create_table() создает таблицу
# book_pages, и функция prepare_book() вставляет записи в эту таблицу.Обратите внимание,
# что использование базы данных
# в вашем проекте может потребовать дополнительных адаптаций в зависимости от конкретных требований
# и структуры вашего проекта.