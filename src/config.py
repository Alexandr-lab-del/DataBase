def config():
    """Функция для подключения к БД"""
    return {
        "dbname": "head",
        "user": "postgres",
        "password": "8695",
        "host": "localhost",
        "port": "5432"
    }

    """Хотел с помощью .env. сделать подключение к БД, но вылазит ошибка:
    package containing module 'dotenv' is not listed in the project requirements"""

# import os
# from dotenv import load_dotenv
#
#
# load_dotenv()
# """Загрузка переменных окружения из файла .env"""
#
#
# def config():
#     """Функция для получения словаря с данными для подключения к БД"""
#     return {
#         "dbname": os.getenv("DB_NAME"),
#         "user": os.getenv("DB_USER"),
#         "password": os.getenv("DB_PASSWORD"),
#         "host": os.getenv("DB_HOST")
#     }
