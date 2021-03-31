from get_url import get_url
import requests
from bs4 import BeautifulSoup


def xml_parsing():
    xml_url = get_url()
    for xml_url in xml_url:
        print(xml_url)
        response = requests.get(xml_url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, features='lxml')
        village = soup.find_all('ukrnas')

        second_village = soup.find_all('Dokyment')

        province = soup.find_all("gybernia")

        county = soup.find_all("povit")

        church = soup.find_all("nasvizerkov")

        fond = soup.find_all("fond")

        inventory = soup.find_all("opis")

        case = soup.find_all("sprava")

        confession = soup.find_all("spovid")

        archive = 'ЦДІАК'

        print(archive)
        fond_list = []
        case_list = []
        confession_list = []
        inventory_list = []
        for confession in confession:
            confession = confession.text
            confession_list.append(confession)
        for village in village:
            village = village.text
            a, b = (str(village)[str(village).find(","):]), (str(village)[:str(village).find(",")])
            village = a + " " + b
            village = village.replace(', ', '')
            village = village.replace(r',', '')
            print(village)

        for second_village in second_village:
            second_village = second_village.text
            print("second= " + second_village)

        for province in province:
            province = province.text
            print(province + ' губернія')

        for county in county:
            county = county.text
            print(county)

        for church in church:
            church = church.text
            print(church)

        for fond in fond:
            fond = fond.text
            fond_list.append(fond)

        for inventory in inventory:
            inventory = inventory.text
            inventory_list.append(inventory)

        for case in case:
            case = case.text
            case_list.append(case)


if __name__ == '__main__':
    print(xml_parsing())
