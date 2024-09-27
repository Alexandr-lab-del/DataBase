import psycopg2
from src.config import config


class DBManager:
    """Класс для подключения к БД"""

    def __init__(self):
        params = config()
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """Получает список компаний и вакансий"""
        self.cur.execute("""
            SELECT employer_name, COUNT(*) as vacancy_count
            FROM vacancies
            GROUP BY employer_name
            ORDER BY vacancy_count DESC
        """)
        return self.cur.fetchall()

    def get_all_vacancies(self):
        """Получает список вакансий со следующими переменными (названия компании и
        вакансии, зарплата и ссылка на вакансию)"""
        self.cur.execute("""
            SELECT employer_name, vacancy_name, salary, vacancy_url
            FROM vacancies
            WHERE salary IS NOT NULL AND salary != 0
            ORDER BY salary DESC
        """)
        return self.cur.fetchall()

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        self.cur.execute("""
            SELECT AVG(salary)
            FROM vacancies
            WHERE salary IS NOT NULL AND salary != 0
        """)
        result = self.cur.fetchone()
        return round(result[0], 2) if result[0] else 0

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней"""
        avg_salary = self.get_avg_salary()
        self.cur.execute("""
            SELECT vacancy_name, salary
            FROM vacancies
            WHERE salary > %s
            ORDER BY salary DESC
        """, (avg_salary,))
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        self.cur.execute("""
            SELECT vacancy_name, salary, vacancy_url
            FROM vacancies
            WHERE LOWER(vacancy_name) LIKE LOWER(%s)
        """, (f'%{keyword}%',))
        return self.cur.fetchall()
