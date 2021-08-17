import requests
from bs4 import BeautifulSoup

con = 'https://music.bugs.co.kr/chart'

doc = requests.get(con, 'html.parser')

soup = BeautifulSoup(doc.text, 'html.parser')

artist = soup.findAll('p', {'class':'artist'})
print(artist)

for title in artist:
    print(title.text.strip().split('\n'))
    print('******************')