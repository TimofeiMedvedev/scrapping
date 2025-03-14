import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
}

# def get_soup(url):
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'lxml')  # html.parser
#     return soup



for count in range(1, 2):
    sleep(3)
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')  # html.parser
    data = soup.find_all('div', class_='w-full rounded border')
    for i in data:
        card_url = i.find('a').get('href')
        list_card_url.append('https://scrapingclub.com' + card_url)
        # name = i.find('h4').text.replace('\n', '')
        # price = i.find('h5').text
        # url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')
        # print(name + '\n' + price + '\n' + url_img + '\n\n')
for item_url in list_card_url:
    response = requests.get(item_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')  # html.parser
    data = soup.find('div', class_='my-8 w-full rounded border')
    name = data.find('h3', class_='card-title').text
    price = data.find('h4', class_='my-4 card-price').text
    text = data.find('p', class_='card-description').text
    url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top').get('src')
    print(name + '\n' + price + '\n' + text + '\n' + url_img + '\n\n')
    


