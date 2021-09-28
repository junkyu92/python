from youtube_api import YouTubeDataAPI
import re


api_key = 'AIzaSyDZ-7SXpoGbbqN4rygir7HUxONPv99wOO4'
yt = YouTubeDataAPI(api_key)

playlist = yt.get_playlists('UCqk5VnwjLfuNs3rm4_12vQA')
#print(playlist)

a = yt.get_videos_from_playlist_id('PLX8wQ_WYl-KUkbO-fIdV-IQCwzQin60Dk')
#print(a)
vidlist = []
for i in range(len(a)):
    vid = a[i].get('video_id')
    vidlist.append(vid)

video_list=[]
for i in range(len(vidlist)):
    video = yt.get_video_metadata(vidlist[i])
    video_list.append(video)

print(video_list)
title_list = []
url_list = []
for i in range(len(video_list)):
    title_list.append(video_list[i]['video_title'])
    url_list.append('https://www.youtube.com/watch?v='
                    + video_list[i]['video_id']
                    + '&list=PLX8wQ_WYl-KUkbO-fIdV-IQCwzQin60Dk&index='
                    + str(i+1))
print(title_list)

# artists2 = []
# titles2 = []
# p = re.compile('(?P<artist>.+)\s+-\s+(?P<title>.+)')
# for i in range(len(title_list)):
#     m = p.search(title_list[i])
#     print(m.group('artist'))
#     print(m.group('title'))
#     artists2.append(m.group('artist'))
#
# print(artists2)

artists = []
titles = []
for i in range(len(title_list)):
    a = title_list[i].split('-')
    artists.append(a[0].strip())
    titles.append(a[1].strip())

print(artists)
print(titles)
print(url_list)

import cx_Oracle
import os

LOCATION = r"C:\Users\kkzz0\Downloads\instantclient_19_12"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]
OracleConnect = cx_Oracle.connect("world42", "1234", "localhost:1521/xe")
OracleCursor = OracleConnect.cursor()

oracleSql = f"""
    insert into BGM values (SEQ_BGM.NEXTVAL, :1, :2, :3)
"""
#print(oracleSql)
for i in range(len(titles)):
    OracleCursor.execute(oracleSql, (titles[i], artists[i], url_list[i]))

OracleCursor.close()
OracleConnect.commit()
OracleConnect.close()