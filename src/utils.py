from src.hh_api_class import HeadHunterAPI
from sql.config import config
from sql.DBmanager_class import DBManager
from sql.create_db import create_db_and_tables, insert_data
from src.company_id import companies_id

def main():
    """
    Функция взаимодействия с пользователем

    """
    params = config()
    message = input("Программа для работы с базой данных вакансий HH приветствует Вас, "
                       "для старта нажмите ENTER")
    hh = HeadHunterAPI()
    data = []
    for emp_id in companies_id:
        vac_data = hh.get_vacancies(emp_id)
        data.extend(vac_data)
    print(len(data))
    db_name = input('Для начала работы придумайте название базы данных:').lower()
    create_db_and_tables(db_name, params)
    insert_data(db_name, data, params)
    db = DBManager(db_name)
    while True:
        user_input = input("Для получения количества вакансий в компаниях введите 1\n"
                        "Для вывода всех вакансий введите 2\n"
                        "Для вывода средней заработной платы по вакансиям введите 3\n"
                        "Для вывода вакансий с з\п выше средней введите 4\n"
                        "Для вывода вакансий по ключевому слову введите 5\n"
                        "Для выхода из программы введите quit: "
                        )
        if user_input == '1':
            db.get_companies_and_vacancies_count(db_name, params)
        elif user_input == '2':
            db.get_all_vacancies(db_name, params)
        elif user_input == '3':
            db.get_avg_salary(db_name, params)
        elif user_input == '4':
            db.get_vacancies_with_higher_salary(db_name, params)
        elif user_input == '5':
            keyword = input("Введите ключевое слово для поиска:")
            db.get_vacancies_with_keyword(db_name, keyword, params)
        elif user_input == 'quit':
            quit("работа с программой закончена")