import psycopg2

class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_companies_and_vacancies_count(self, db_name, params):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        with psycopg2.connect(dbname=db_name, **params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT COUNT(*), employeers.name 
                FROM vacancies
                INNER JOIN employeers USING(emp_id) 
                GROUP BY employeers.name
                """)
                rows = cur.fetchall()
                for row in rows:
                    print(row)



    def get_all_vacancies(self, db_name, params):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и
        зарплаты и ссылки на вакансию.
        """
        with psycopg2.connect(dbname=db_name, **params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT name, salary_from, salary_to, url, employeers.name 
                FROM vacancies
                INNER JOIN employeers USING(emp_id) 
                """)
                rows = cur.fetchall()
                for row in rows:
                    print(row)



    def get_avg_salary(self, db_name, params):
        """
        Метод получает среднюю зарплату по вакансиям.
        """
        with psycopg2.connect(dbname=db_name, **params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT AVG(salary_from)
                FROM vacancies
                WHERE salary_from > 0
                """),
                rows = cur.fetchall()
                for row in rows:
                    print(row)




    def get_vacancies_with_higher_salary(self, db_name, params):
        """
        Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        with psycopg2.connect(dbname=db_name, **params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT name, salary_from FROM vacancies
                    WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies
                         WHERE salary_from > 0)
                    """)
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_vacancies_with_keyword(self, db_name, keyword, params):
        """
        Метод получает список всех вакансий, в названии которых содержатся переданные в метод
        слова, например “python”.
        """
        with psycopg2.connect(dbname=db_name, **params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM vacancies
                    WHERE name LIKE '%{keyword}%'
                    """)
                rows = cur.fetchall()
                for row in rows:
                    print(row)