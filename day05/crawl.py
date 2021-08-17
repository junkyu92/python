import requests
from bs4 import BeautifulSoup

targetsite = 'https://music.bugs.co.kr/chart'

doc = requests.get(targetsite)
# print(doc)

html = doc.text
# print(html)

soup = BeautifulSoup(html, 'html.parser')
#print(soup)

titles = soup.findAll('p', {'class':'title'})
print(titles)

for title in titles:
    print(title.text.strip())
