"""
This big module parsing data from get xml page using beautiful soup
"""

# project imports
import requests
from bs4 import BeautifulSoup
from random import randint

# local imports
from Connect import connect
from mysql.connector import Error
from get_url import get_url


def listToString(s: list) -> str:
    """
    convert list to string format
    :param s: list
    :return: str
    """
    str1 = ""
    return str1.join(s)


def xml_parsing():
    """
    parse xml page, gets import using beautiful soup and insert to database
    :return:
    """
    xml_url = get_url()
    conn = connect()
    for xml_url in xml_url:
        print(xml_url)
        response = requests.get(xml_url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, features='lxml')
        print(soup)
        village = soup.find_all('ukrnas')
        c = soup.find_all("gyb")
        second_village = soup.find_all('dokyment')
        kostel = soup.find_all('admin1')
        province = soup.find_all("gybernia")

        county = soup.find_all("povit")

        church = soup.find_all("nasvizerkov")

        fond = soup.find_all("fond")
        inventory = soup.find_all("opis")
        case = soup.find_all("sprava")

        confession = soup.find_all("spovid")

        archive = 27
        village_ = ""
        second_village_ = ""
        church_ = ""
        religion = ""
        county_ = ""
        province_ = ""
        a_province_ = ""
        b_province_ = ""
        fond_list = []
        case_list = []
        number_of = randint(30000, 40000)
        confession_list = []
        inventory_list = []
        for c in c:
            c_ = c.text
            a_province_, b_province_ = (str(c_)[str(c_).find(".") + 2:]), (str(c_)[:str(c_).find(".") + 1])
            a_province_ = " " + a_province_
        for confession in confession:
            confession = confession.text
            confession_list.append(confession)
        for village in village:
            village_ = village.text
            a, b = (str(village_)[str(village_).find(","):]), (str(village_)[:str(village_).find(",")])
            village_ = a + " " + b
            village_ = village_.replace(', ', '')
        for second_village in second_village:
            second_village_ = second_village.text

        province_ = a_province_
        county_ = b_province_

        for church in church:
            church_ = "костел " + church.text

        for fond in fond:
            fond = fond.text
            if fond == '':
                fond = "назва фонду не вказана"
            fond_list.append(fond)

        for inventory in inventory:
            inventory = inventory.text
            if inventory == '':
                inventory = "назва опису не вказана"
            inventory_list.append(inventory)

        for case in case:
            case = case.text
            case_list.append(case)
        metric = []
        try:
            for i in range(len(case_list)):
                metric.append(listToString(confession_list[i]) + ", Фонд " + listToString(
                    fond_list[i]) + ', ' + "Опис " + listToString(
                    inventory_list[i]) + " справа:" + listToString(
                    case_list[i]) + ";")
        except:
            print(village_)
        spovid = []
        clirova = []
        final_metrics = []
        for i in range(len(metric)):
            m = listToString(metric[i])
            if m.find('сповідний') != -1 or m.find('cповідний') != -1:
                spovid.append(metric[i])
            elif m.find('клірова') != -1:
                clirova.append(metric[i])
            elif m.find('візитація') != -1:
                spovid.append(metric[i])
            elif m.find('Візитація') != -1:
                spovid.append(metric[i])
            else:
                final_metrics.append(metric[i])
        metric_ = listToString(final_metrics)
        spovid_ = listToString(spovid)
        religion = "Католицизм"
        clirova_ = listToString(clirova)
        metrics = [(number_of,
                    archive,
                    province_,
                    None,
                    church_,
                    village_,
                    county_,
                    None,
                    second_village_,
                    metric_,
                    metric_,
                    None,
                    metric_,
                    spovid_,
                    clirova_,
                    religion)]
        try:
            query = "INSERT INTO wp_catalog_of_metrics (number_of,archive,province,eparchy,church,village,county, second_province,second_village, birth,wedding,divorce,death,testament,additional, religion) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor = conn.cursor()
            cursor.executemany(query, metrics)
            conn.commit()
        except Error as e:
            print('Error:', e)

        finally:
            cursor.close()

    conn.close()


if __name__ == '__main__':
    print(xml_parsing())
