import requests as re
from bs4 import BeautifulSoup
import csv
import urllib

def get_all_countries():
    '''
    Scrapes wikipedias list of ruling parties by country.
    
    Returns a list of tuples containing:
        COUNTRY NAME: name of the counry
        RULING PARTY: the name of the ruling or dominant party 
        LINK: link to the corresponding wikipedia page of RULING PARTY
    '''

    res = re.get('https://en.wikipedia.org/wiki/List_of_ruling_political_parties_by_country').content

    soup = BeautifulSoup(res, 'html.parser')

    # tables for every letter, starts at index 4 due o other tables present on page
    tables = soup.find_all('tbody')[4:] 

    out_list = []
    
    # iterate over tables
    for table in tables:
        
        # get the rows i.e countries in this table
        rows = table.find_all('tr')[1:] # index 0 is header

        # ierate over all the countries in this table
        for row in rows:
            
            # country name
            country = row.find_all('td')[0].find('a').text
            
            # party info
            party = row.find_all('td')[2]
                        
            party_info =party.find('b')
            #print(party_info)
            #print(country, party_info)

            # ruling party has not link (usually independants)
            if party_info != None:
                if party_info.find('a') == None:
                    #print(party_info)
                    ruling_party = party_info.text
                    link = None
                else:
                    #print(party_info)
                    ruling_party = party_info.find('a').get('title')
                    link = party_info.find('a')['href']
               
            else:
                ruling_party = 'No Parties'
                link = None
                
                # For non partisan political systems and non-democracies ets
                
            
            #print('PARTY', ruling_party)
            out_list.append({'country name': country, 'ruling party': ruling_party, 'url': link})
    return out_list


# ('Mauritius', 'Militant Socialist Movement', '/wiki/Militant_Socialist_Movement')

def get_political_position(url):
    BASE_URL = 'https://en.wikipedia.org'
    
    url = BASE_URL + url
   
    #url = urllib.quote(url.encode('UTF-8')) 
    
    print(url)
    
    response_content = re.get(url).content
    
    #print(response_content)
    
    soup = BeautifulSoup(response_content, 'html.parser')
    
    #print(soup)

    political_position_header = soup.find('a', title="Political spectrum")
    
    political_position = 'N/A'
    
    if political_position_header:
        political_position = political_position_header.parent.parent.find('td').find('a').text
    
    
    return political_position
    
def write_to_csv():
    data = get_all_countries()
    
    for country in data:
        url = country['url']
        print(country)
        country['position'] = get_political_position(country['url']) if url != None else None
    
    with open('data/countries.csv', 'w') as file:
        
        header = data[0].keys()
        
        writer = csv.DictWriter(file, fieldnames=header)
        
        writer.writeheader()
        
        for row in data:
            writer.writerow(row)
            
write_to_csv()