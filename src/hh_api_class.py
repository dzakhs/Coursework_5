import requests

class HeadHunterAPI:
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self,data):
        """
            Метод получения данных о вакансиях с сайта hh.ru по id компании
            param emp_id: id компании для поиска вакансий
            return: список со словарями
        """
        for emp_id in data.values():
            pages = 10
            params = {
                "employer_id" : emp_id,
                "per_page" : 100,
                "area" : 113,
                "only_with_salary" : True

            }

            data = []

            for page in range(pages):

                responce = requests.get(self.url, params=params).json()['items']
                data.extend(responce)

        return data




