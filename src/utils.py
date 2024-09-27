import psycopg2
from src.config import config


def create_database():
    """Создание базы данных и таблиц для сохранения переменных"""
    params = config()
    conn = psycopg2.connect(**params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employers (
            employer_id INTEGER PRIMARY KEY,
            employer_name TEXT NOT NULL,
            employer_area TEXT NOT NULL,
            url TEXT,
            open_vacancies INTEGER
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS vacancies (
            vacancy_id INTEGER PRIMARY KEY,
            vacancy_name VARCHAR,
            vacancy_area VARCHAR,
            salary INTEGER,
            employer_id INTEGER REFERENCES employers(employer_id),
            employer_name VARCHAR,
            vacancy_url VARCHAR
        )
    """)

    conn.close()


def save_data_to_database(data_employer, data_vacancies):
    """Сохранение данных о работодателях и вакансиях"""
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    for employer in data_employer:
        cur.execute("""
            INSERT INTO employers (employer_id, employer_name, employer_area, url, open_vacancies)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (employer_id) DO NOTHING
        """, (
            employer['id'],
            employer['name'],
            employer['area']['name'],
            employer['alternate_url'],
            employer['open_vacancies']
        ))

    for vacancy in data_vacancies:
        salary = vacancy['salary']['from'] if vacancy['salary'] and vacancy['salary']['from'] else None
        cur.execute("""
            INSERT INTO vacancies (vacancy_id, vacancy_name, vacancy_area, salary, employer_id, employer_name, vacancy_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (vacancy_id) DO NOTHING
        """, (
            vacancy['id'],
            vacancy['name'],
            vacancy['area']['name'],
            salary,
            vacancy['employer']['id'],
            vacancy['employer']['name'],
            vacancy['alternate_url']
        ))

    conn.commit()
    conn.close()
