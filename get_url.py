import re

import requests
import bs4


def get_url():
    urls = []
    data = requests.request('get', 'https://cdiak.archives.gov.ua/baza_geog_pok/church.php/')  # any website
    s = bs4.BeautifulSoup(data.text, 'html.parser')
    for link in s.findAll('a'):
        if link.has_attr('href'):
            link = (str(link)[str(link).find("=\"") + 2:str(link).find("\">")])
            urls.append("https://cdiak.archives.gov.ua/baza_geog_pok/" + link)
    return urls


def print_urls(url):
    for i in range(len(url)):
        print(url[i])
    return None


if __name__ == '__main__':
    print_urls(get_url())
