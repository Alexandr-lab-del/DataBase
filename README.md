# Проект по работе с API HeadHunter и базой данных PostgreSQL

Этот проект позволяет получать данные о компаниях и вакансиях с сайта hh.ru, сохранять их в базу данных PostgreSQL и выполнять различные запросы к этим данным.

## Описание проекта

Проект состоит из нескольких Python-скриптов, которые выполняют следующие функции:
- Получение данных о работодателях и вакансиях с API HeadHunter
- Сохранение полученных данных в PostgreSQL базу данных
- Предоставление пользовательского интерфейса для выполнения запросов к базе данных

## Требования

- Python 
- PostgreSQL
- Библиотеки: requests, psycopg2

## Установка и настройка

1. Клонируйте репозиторий:
- https://github.com/Alexandr-lab-del/DataBase/tree/course_work
2. Установите необходимые библиотеки:
- pip install requests, psycopg2

3. Настройте подключение к базе данных в файле `src/config.py`:
```python
   def config():
       return {
           "dbname": "your_database_name",
           "user": "your_database_user",
           "password": "your_database_password",
           "host": "your_database_host"
       }
