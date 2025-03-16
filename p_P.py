import requests
from bs4 import BeautifulSoup
from time import sleep

# list_card_url = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
}

def download(url):
    resp = requests.get(url, stream=True)
    r = open(r"/home/timofey/Documents/", "wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close
def get_soup(url):
    response = requests.get(url, headers=headers)
    sleep(3)
    soup = BeautifulSoup(response.text, 'lxml')  # html.parser
    return soup

def get_url():
    for count in range(1, 2):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        data = get_soup(url).find_all('div', class_='w-full rounded border')
        for i in data:
            card_url = 'https://scrapingclub.com' + i.find('a').get('href')
            yield card_url

def array():
    for item_url in get_url():
        data = get_soup(item_url).find('div', class_='my-8 w-full rounded border')
        name = data.find('h3', class_='card-title').text
        price = data.find('h4', class_='my-4 card-price').text
        text = data.find('p', class_='card-description').text
        url_img = 'https://scrapingclub.com' + data.find(
            'img', class_='card-img-top'
        ).get('src')
        yield name, price, text, url_img