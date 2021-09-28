# url = 'https://www.youtube.com/playlist?list=PLX8wQ_WYl-KUkbO-fIdV-IQCwzQin60Dk'
# 재생목록에서 가수, 곡명, url 추출해서 배열에 넣기


from bs4 import BeautifulSoup
import requests


url = 'https://www.youtube.com/playlist?list=PLX8wQ_WYl-KUkbO-fIdV-IQCwzQin60Dk'
site = requests.get(url)
content = BeautifulSoup(site.content, 'html.parser')

title = content.find_all('a', {'id':'video-title'})
print(title)




