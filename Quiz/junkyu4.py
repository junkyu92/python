#승률 55%가 넘는 사람 프린트
import requests
from bs4 import BeautifulSoup

con = 'https://www.op.gg/ranking/ladder/'

doc = requests.get(con, 'html.parser')

soup = BeautifulSoup(doc.text, 'html.parser')

trData = soup.findAll('tr', 'ranking-table__row')

# print(trData)
rowList = []
columnList = []

for i in range(0, len(trData)):
    tdData = trData[i].find_all('td')
    # print(tdData)
    for j in range(0, 6):
        element = tdData[j].text
        # print(element)
        columnList.append(element)

    rowList.append(columnList)
    columnList = []
print(rowList)

count = 0
for i in range(0, len(rowList)):
    ratio = rowList[i][5][-3:-1]
    if int(rowList[i][5][-3:-1]) > 55:
        count += 1
print(count)
