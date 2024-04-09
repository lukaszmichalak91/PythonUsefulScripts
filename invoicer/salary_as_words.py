import requests

api_ulr = "https://api.officeblog.pl/slownie.php"


def get_salary_words(salary):
    return requests.get(api_ulr, params={"format": "2", "kwota": f"{salary}"}).text
