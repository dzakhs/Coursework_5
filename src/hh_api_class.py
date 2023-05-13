import requests

class HeadHunterAPI:
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword):
        """
        метод получения данных о вакансиях с сайте
        :param keyword: ключевое слово для поиска вакансий
        :return: список со словарями
        """
        pages = 10
        params = {
            "text" : keyword,
            "per_page" : 100,
            "area" : 113,
            "only_with_salary" : True

        }

        data = []

        for page in range(pages):

            responce = requests.get(self.url, params=params).json()['items']
            data.extend(responce)

        return data
