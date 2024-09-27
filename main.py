from src.func import HH
from src.manager import DBManager
from src.utils import create_database, save_data_to_database


def main():
    """Основноц функционал"""
    create_database()

    hh = HH()
    data_employer = hh.get_employers()
    data_vacancies = hh.load_vacancies()

    save_data_to_database(data_employer, data_vacancies)

    db_manager = DBManager()

    print("""
    Что конкретно вас интересует?:
    0 - Завершить действие
    1 - Получить список всех компаний и их вакансий
    2 - Получить список вакансий со следующими переменными (названия компании и вакансии, зарплата и ссылка на вакансию)
    3 - Получить среднюю зарплату по вакансиям
    4 - Получить список всех вакансий, у которых зарплата выше средней
    5 - Получить список всех вакансий, в названии которых содержатся переданные в метод слова
    """)

    while True:
        user_input = input("Что вас интересует? Введите цифру от 0 до 5: ")

        if user_input == "0":
            print("Программа завершена")
            break
        elif user_input == "1":
            companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
            print("Список всех компаний и их вакансий:")
            for company, count in companies_and_vacancies_count:
                print(f"{company}: {count} вакансий")
        elif user_input == "2":
            all_vacancies = db_manager.get_all_vacancies()
            print("Список всех вакансий:")
            for vacancy in all_vacancies:
                print(f"Компания: {vacancy[0]}, Вакансия: {vacancy[1]}, Зарплата: {vacancy[2]}, Ссылка: {vacancy[3]}")
        elif user_input == "3":
            avg_salary = db_manager.get_avg_salary()
            print(f"Средняя зарплата по вакансиям: {avg_salary}")
        elif user_input == "4":
            higher_salary_vacancies = db_manager.get_vacancies_with_higher_salary()
            print("Вакансии с зарплатой выше средней:")
            for vacancy in higher_salary_vacancies:
                print(f"Вакансия: {vacancy[0]}, Зарплата: {vacancy[1]}")
        elif user_input == "5":
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            keyword_vacancies = db_manager.get_vacancies_with_keyword(keyword)
            print(f"Вакансии, содержащие '{keyword}' в названии:")
            for vacancy in keyword_vacancies:
                print(f"Вакансия: {vacancy[0]}, Зарплата: {vacancy[1]}, Ссылка: {vacancy[2]}")
        else:
            print("Неверный ввод. Пожалуйста, введите число от 0 до 5.")


if __name__ == '__main__':
    main()
