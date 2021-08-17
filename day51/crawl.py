from bs4 import BeautifulSoup
import requests
from opgg_DAO import *

url = 'https://www.op.gg/ranking/ladder/page=2'
doc = requests.get(url)
soup = BeautifulSoup(doc.text, 'html.parser')

# print(soup)

trData = soup.findAll('tr', 'ranking-table__row')

rowList = []
columnList = []

for i in range(0, len(trData)):
    tdData = trData[i].find_all('td')

    for j in range(0, 5):
        element = tdData[j].text
        columnList.append(element)

    rowList.append(tuple(columnList))
    columnList = []

vo = rowList

# Opgg.insert(vo)     #입력
#
# Opgg.read()         #read

result = Opgg.read()

for i in range(0, len(result)):
    if result[i]['rank'] == '168':
        print(result[i]['name'])