import requests
from bs4 import BeautifulSoup
import datetime

url = "http://www.kleague.com/schedule"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

s = soup.find_all('tr', {'id':'2020-05-08n'})
print(s)
