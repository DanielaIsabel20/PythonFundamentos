import requests


url = 'https://quotes.toscrape.com/'
response = requests.get(url)


with open('page.html', 'w', encoding='utf-8') as f:
    f.write(response.text)