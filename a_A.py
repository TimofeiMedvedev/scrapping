from requests import Session
from bs4 import BeautifulSoup
from time import sleep


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
}

work = Session()

work.get('https://quotes.toscrape.com/', headers=headers)
response = work.get('https://quotes.toscrape.com/login', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
token = soup.find('form').find('input').get('value')

data = {
    'csrf_token': token,
    'username': 'noname',
    'password': 'password'
}
result = work.post(
    'https://quotes.toscrape.com/login',
    headers=headers, data=data,
    allow_redirects=True
)

result = soup.find_all('span', class_='text')
author = soup.find_all('small', class_='author')




