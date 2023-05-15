import psycopg2

class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
    pass

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и
        зарплаты и ссылки на вакансию.
        """
    pass

    def get_avg_salary(self):
        """
        получает среднюю зарплату по вакансиям.
        """
    pass


    def get_vacancies_with_higher_salary(self):
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
    pass

    def get_vacancies_with_keyword(self):
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод
        слова, например “python”.
        """
    pass