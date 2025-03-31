import requests

url = 'https://scrapingclub.com/exercise/ajaxdetail/'
response = requests.get(url).json()


print(response["title"])
print(response["price"])
print(response["description"])
print(response)