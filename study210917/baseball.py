import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo'
site = requests.get(url)
content = BeautifulSoup(site.content, 'html.parser')
rank = content.select('div.tbl_box tbody#regularTeamRecordList_table tr th')
name = content.select('div.tbl_box tbody#regularTeamRecordList_table tr td.tm span')

games=[]
for x in range(0,10):
    location = 'div.tbl_box table tbody tr td:nth-of-type(2) span'
    games.append(int(content.select(location)[x].text))
#print(games)

wins=[]
for x in range(0,10):
    location = 'div.tbl_box tbody#regularTeamRecordList_table tr td:nth-of-type(3) span'
    wins.append(int(content.select(location)[x].text))
print(wins)

ranks=[]
for x in rank:
    ranks.append(int(x.string))
names=[]
for x in name:
    names.append(x.string)

df = pd.DataFrame({'순위':ranks, '구단명':names, '게임수':games, '승리':wins})
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
plt.xlabel('구단명')
plt.ylabel('순위')
plt.plot(df['구단명'], df['순위'])
plt.show()