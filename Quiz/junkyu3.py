#t1 gumayusi가 랭킹 몇윈지 프린트

import requests
from bs4 import BeautifulSoup

con = 'https://www.op.gg/ranking/ladder/'

doc = requests.get(con, 'html.parser')

soup = BeautifulSoup(doc.text, 'html.parser')

trData = soup.findAll('tr', 'ranking-table__row')

rowList = []
columnList = []

for i in range(0, len(trData)):
    tdData = trData[i].find_all('td')

    for j in range(0, 2):
        element = tdData[j].text
        columnList.append(element)

    rowList.append(columnList)
    columnList = []

# print(rowList)
# print(rowList[0])
# print(rowList[0][1])

for i in range(0, len(rowList)):
    if rowList[i][1] == 'T1 Gumayusi':
        print(rowList[i][1], '의 순위는', rowList[i][0], '위입니다.')
print()

id = input('아이디를 입력해주세요.>>')
for i in range(0, len(rowList)):
    if rowList[i][1] == id:
        print(rowList[i][1], '의 순위는', rowList[i][0], '위입니다.')
