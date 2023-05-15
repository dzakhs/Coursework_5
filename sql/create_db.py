import psycopg2


def create_db_and_tables(db_name, params):
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    conn.close()

    conn = psycopg2.connect(dbname=db_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE employeers (
                    emp_id SERIAL PRIMARY KEY,
                    name varchar(100) NOT NULL,
                    emp_url varchar (255) NOT NULL
                )
            """)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE vacancies (
                    id SERIAL PRIMARY KEY,
                    emp_id INT REFERENCES employeers(id),
                    name varchar(255) NOT NULL,
                    url varchar(255) NOT NULL,
                    salary_from int NOT NULL,
                    salary_to int NOT NULL,
                    experience varchar(150),
                    description text
                )
            """)

    conn.commit()
    conn.close()


def insert_data(db_name, data, params):
    conn = psycopg2.connect(dbname=db_name, **params)

    with conn.cursor() as cur:
        for vacancy in data:
            salary_from = vacancy['salary']['from'] if vacancy['salary']['from'] is not None else 0
            salary_to = vacancy['salary']['from'] if vacancy['salary']['from'] is not None else 0
            cur.execute("""
             INSERT INTO vacancies(emp_id, name, url, salary_from, salary_to, experience, description)
             VALUES (%s, %s, %s, %s, %s, %s, %s)
             """,
                        (vacancy['empoloyer']['id'], vacancy['name'], vacancy['alternate_url'], salary_from, salary_to,
                         vacancy['experience']['name'], vacancy['snippet']['responsibility']))

            cur.execute("""
             INSERT INTO empoyeers(emp_id, name, url)
             VALUES (%s, %s, %s)
             """,
                        (vacancy['employer']['id'], vacancy['employer']['name'], vacancy['employer']['alternate_url']))

        conn.commit()
        conn.close()