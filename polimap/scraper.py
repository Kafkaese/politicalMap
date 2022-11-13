import requests as re
from bs4 import BeautifulSoup


def get_all_countries():
    

    res = re.get('https://en.wikipedia.org/wiki/List_of_ruling_political_parties_by_country').content

    soup = BeautifulSoup(res, 'html.parser')

    tables = soup.find_all('tbody')[6:] 

    for table in tables:
        rows = table.find_all('tr')[1] # index 0 is header

        countries = rows.find_all('td')[0].find('a').text
        parties = rows.find_all('td')[2]

        party_info =parties.find('b')
        #print(party_info)
        
        ruling_party = party_info.find('a').get('title', 'No Parties') if party_info != None else None
        
        # For non partisan political systems
        link = party_info.find('a')['href'] if party_info != None else None
        
        #print('PARTY', ruling_party)
        print(countries, ruling_party, link)

get_all_countries()