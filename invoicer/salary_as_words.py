import requests

api_ulr = "https://api.officeblog.pl/slownie.php"


def get_salary_words(salary_gross):

    salary_in_words = requests.get(api_ulr, params={"format": "3", "kwota": f"{salary_gross}"}).text
    salary_in_words = salary_in_words.replace("złotych", "PLN").replace("złote", "PLN")
    return salary_in_words


if __name__ == "__main__":
    print(get_salary_words("32,23"))
