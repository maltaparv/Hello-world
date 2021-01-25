import requests
from bs4 import BeautifulSoup
import pandas as pd

bank_id = 1771062  # ID банка на сайте banki.ru
page = 1
max_page = 10

url = 'https://www.banki.ru/services/questions-answers/?id=%d&p=1' % (bank_id)  # url страницы
# r = requests.get(url)
# with open('test.html', 'w') as output_file:
#   output_file.write(r.text)

result = pd.DataFrame()

r = requests.get(url)  # отправляем HTTP запрос и получаем результат
soup = BeautifulSoup(r.text)  # тправляем полученную страницу в библиотеку для парсинга
tables = soup.find_all('table', {'class': 'qaBlock'})  # Получаем все таблицы с вопросами
for item in tables:
    res = pd.parse_table(item)
