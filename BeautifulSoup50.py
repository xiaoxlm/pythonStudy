import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.python.org/events/python-events/')
soup = BeautifulSoup(resp.text, 'html.parser')

for li in soup.select('.list-recent-events > li'):
    print('title:', li.find('a').text)
    print('time:', li.find('time').text)
    print('location:', li.select_one('.event-location').text)
    print('*' * 100)