import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path


def html_parser(class_id):
    # fetch data using html.parser
    response = requests.get('http://122.160.230.125:8080/gbod/gb_on_demand.do')
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('div', class_=class_id).get_text().strip()
    return data


def create_newfile():
    # create new file
    DSL_ID = html_parser("Dslaccount")
    MonthlyQuota = html_parser("DatablockSectionSecond")
    with open('DataTracking.txt', 'w') as newfile:
        newfile.writelines(("DSL_ID:  {}      MonthlyQuota: {}\n\n      Date         Time                   DataLeft               DaysLeft \n").format(DSL_ID[-16:], MonthlyQuota[-6:]))


if not Path('./DataTracking.txt').is_file():
    # check whether file exits or not
    create_newfile()


DataUsage = html_parser("DatablockSectionSecond")
DaysLeft = html_parser("DatablockSectionThird accordianblock")


with open('DataTracking.txt', 'a') as f:
    # write fetched data to file
        f.writelines('   {}     |       {}      |           {}\n'.format(datetime.now(), DataUsage[-19:18], DaysLeft))
