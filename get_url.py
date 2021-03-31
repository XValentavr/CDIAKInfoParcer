import requests
from bs4 import BeautifulSoup, SoupStrainer

url = 'https://cdiak.archives.gov.ua/baza_geog_pok/church.php'
r = requests.get(url)
urls = []
soup = BeautifulSoup(r.content, 'html.parser', parse_only=SoupStrainer('a'))
for link in soup:
    if link.has_attr('href'):
        urls.append(link['href'])
start = 28
for start in range(len(urls)):
    if start >= 28:
        print(urls[start])
