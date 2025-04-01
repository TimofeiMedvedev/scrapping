import requests
from bs4 import BeautifulSoup
from time import sleep
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"
}

# list_card_url = []

def get_url():

    for count in range(1, 3):
    
        url = f'https://pro-kaminy.ru/katalog/pechi/pechi-kaminyi/fireway/?page={count}'
    
        response = requests.get(url, headers=headers)
    
        soup = BeautifulSoup(response.text, 'lxml')  # html.parser
        data = soup.find_all('div', class_='item product-item')
    
        for i in data:
            card_url = 'https://pro-kaminy.ru/' + i.find('a').get('href')
            # list_card_url.append(card_url)
            yield card_url

def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(5)
        soup = BeautifulSoup(response.text, 'lxml')  # html.parser
        data = soup.find('div', class_='page')
        img_url = data.find_all('img')
        name = data.find('h1', class_='pl40').text
        price = data.find('div', class_='price-val').find('span').text
        product_cod = data.find('div', class_='product-code').text.lstrip(
            'Код товара:'
        )
        availability = data.find('div', class_='product-order-top').text.split()
        if 'наличии' in availability:
            availability = '1'
        else:
            availability = '0'
        img_urls_full = []
    
        for img in img_url:
            img_src = img.get('src')
            if '150x150' in img_src:
                img_new = 'https://pro-kaminy.ru' + img_src.replace('150x150/', '')
                img_urls_full.append(img_new)
    
        img_urls_full_format = '; '.join(img_urls_full)
        characteristics = data.find_all('div', class_='features-list__row')
        dict_characteristics = {}
        for item_haracteristics in characteristics:
            item_key = item_haracteristics.find(
                'div', class_='features-list__title'
            ).text.strip()
            item_value = item_haracteristics.find(
                'div', class_='features-list__value'
            ).text.replace('\n', '')
            dict_characteristics[item_key] = item_value
        manufacturer = dict_characteristics.get('Производитель:', '').strip()
        country_manufacturer = dict_characteristics.get(
            'Страна производитель:', ''
        ).strip()
        power = ''.join(re.findall(r"\d+", dict_characteristics.get(
            'Мощность:', ''
        )))
        kpd = ''.join(re.findall(r"\d+", dict_characteristics.get(
            'Коэффициент полезного действия (КПД):', ''
        )))
        finishing_material = dict_characteristics.get(
            'Облицовочный материал:', ''
        ).strip()
        manufacturing_material = dict_characteristics.get(
            'Материал топки:', ''
        ).strip()
        side_chimney = dict_characteristics.get('Выход дымохода:', '').strip()
        area_of_the_room = ''.join(re.findall(r"\d+", dict_characteristics.get(
            'Площадь обогрева:', ''
        ))).rstrip('2')
        glass_on_the_door = dict_characteristics.get(
            'Наличие стекла в дверце:', ''
        ).strip()
        if glass_on_the_door == 'Да':
            glass_on_the_door = 'Есть'
        else:
            glass_on_the_door = 'Нет'
    
        weight = ''.join(re.findall(r"\d+", dict_characteristics.get('Вес:', '')))
        warranty = ' '.join(dict_characteristics.get(
            'Гарантийный срок:', ''
        ).split())
        width = ''.join(re.findall(r"\d+", dict_characteristics.get(
            'Ширина:', ''
        )))
        height = ''.join(re.findall(r"\d+", dict_characteristics.get(
            'Высота:', ''
        )))
        depth = ''.join(re.findall(r"\d+", dict_characteristics.get(
            'Глубина:', ''
        )))
        diameter = ''.join(re.findall(
            r"\d+", dict_characteristics.get('Диаметр:', '')
        ))
        clean_gorenje = dict_characteristics.get(
            'Система чистого горения:', ''
        ).strip()
        if clean_gorenje == 'Да':
            clean_gorenje = 'Есть'
        else:
            clean_gorenje = 'Нет'
        volume_room = ''.join(re.findall(r"\d+", dict_characteristics.get(
            'Объем отапливаемого помещения:', ''
        ))).rstrip('3')
        types_of_fuel = dict_characteristics.get(
            'Виды твердого топлива:', ''
        ).strip()
        product_url = card_url
        yield (name, price, img_urls_full_format, product_cod, manufacturer,
               country_manufacturer, power, kpd, finishing_material,
               manufacturing_material, side_chimney, area_of_the_room,
               glass_on_the_door, weight, warranty, width, height, depth,
               diameter, clean_gorenje, volume_room, types_of_fuel,
               product_url, availability)
        # print(name + '\n' + price + '\n' + img_urls_full_format + '\n' + manufacturer +
        #       '\n' + country_manufacturer + '\n' + power + '\n' + kpd + '\n' +
        #       finishing_material + '\n' + manufacturing_material + '\n' +
        #       side_chimney + '\n' + area_of_the_room + '\n' + glass_on_the_door +
        #       '\n' + weight + '\n' + warranty + '\n' + width + '\n' + height + '\n' +
        #       depth + '\n' + diameter + '\n' + clean_gorenje + '\n' + volume_room + 
        #       '\n' + types_of_fuel + '\n' + product_url + '\n' + availability +
        #       '\n' + product_cod)

# 2. Вариант парсинга со страницы карточек товара всех товаров

# for count in range(1, 3):

#     url = f'https://pro-kaminy.ru/katalog/pechi/pechi-kaminyi/fireway/?page={count}'

#     response = requests.get(url, headers=headers)

#     sleep(3)

#     soup = BeautifulSoup(response.text, 'lxml')  # html.parser
#     data = soup.find_all('div', class_='item product-item')

#     for i in data:
#         name = i.find('div', class_='product-item-top').text.replace('\n', '')
#         name_rm = name.replace('П', 'п')
#         name_full = 'Чугунная ' + name_rm
#         price = i.find('div', class_='price-wr').text.replace('₽', '')
#         url_img_teg = i.find('div', class_='product-item-img')
#         url_img = url_img_teg.find('img').get('src')
#         url_img_full = 'https://pro-kaminy.ru' + url_img

#         print(name_full + '\n' + price + '\n' + url_img_full + '\n\n')

# 1. Вариант парсинга со страницы карточек товара одной карточки

# name = data.find('div', class_='product-item-top').text.replace('\n', '')
# name_rm = name.replace('П', 'п')
# name_full = 'Чугунная ' + name_rm
# price = data.find('div', class_='price-wr').text.replace('₽', '')
# url_img_teg = data.find('div', class_='product-item-img')
# url_img = url_img_teg.find('img').get('src')
# url_img_full = 'https://pro-kaminy.ru' + url_img

# print(name_full + '\n' + price + '\n' + url_img_full + '\n\n')
