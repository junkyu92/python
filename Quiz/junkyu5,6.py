# url = 'https://www.op.gg/ranking/ladder/page=2'
# DB와 opgg_DAO 필요
#
# 5. 위 사이트에서 랭킹,이름,티어,포인트,레벨을 크롤링해서 DB에 넣기
# 6. DB에 넣은 것을 읽어와서 150위의 이름을 출력


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
        element = tdData[j].text.replace("\t","").replace("\n","")
        columnList.append(element)

    rowList.append(tuple(columnList))
    columnList = []

vo = rowList

# Opgg.insert(vo)     #입력
#
# Opgg.readAll()         #read
#
# result = Opgg.readAll()
#
# for i in range(0, len(result)):
#     if result[i]['rank'] == '150':
#         print(result[i]['name'])
#
# Opgg.read('150')

