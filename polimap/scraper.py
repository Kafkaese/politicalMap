import requests as re
from bs4 import BeautifulSoup

res = re.get('https://en.wikipedia.org/wiki/List_of_ruling_political_parties_by_country').content

soup = BeautifulSoup(res, 'html.parser')

print(soup)
