import requests
import bs4


def get_url():
    urls = []
    data = requests.request('get', 'https://cdiak.archives.gov.ua/baza_geog_pok/church.php/')
    s = bs4.BeautifulSoup(data.text, 'html.parser')
    for link in s.findAll('a'):
        if link.has_attr('href'):
            if str(link).find("href=\"") == 20:
                continue
            else:
                link = (str(link)[str(link).find("=\"") + 2:str(link).find("\">")])
                urls.append("https://cdiak.archives.gov.ua/baza_geog_pok/" + link)
    return urls
