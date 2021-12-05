"""
This module gets a href url from site page
"""

# project imports
import requests
import bs4


def get_url():
    """
    get a href urls from page
    :return: set
    """
    urls = []
    data = requests.request('get', 'https://cdiak.archives.gov.ua/baza_geog_pok/decanats.php')
    s = bs4.BeautifulSoup(data.text, 'html.parser')
    for link in s.findAll('a'):
        if link.has_attr('href'):
            if str(link).find("href=\"") == 20:
                continue
            else:
                link = (str(link)[str(link).find("=\"") + 2:str(link).find("\">")])
                urls.append("https://cdiak.archives.gov.ua/baza_geog_pok/" + link)
    unique = set(urls)
    return unique
