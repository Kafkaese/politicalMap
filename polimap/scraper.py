import requests as re
from bs4 import BeautifulSoup

res = re.get('https://en.wikipedia.org/wiki/List_of_ruling_political_parties_by_country').content

soup = BeautifulSoup(res, 'html.parser')

tables = soup.find_all('tbody')[6] 

rows = tables.find_all('tr')[1] # index 0 is header

parties = rows.find_all('td')[2]

ruling_party, link = parties.find('b').find('a').get('title'), parties.find('b').find('a')['href']

print(ruling_party, link)
