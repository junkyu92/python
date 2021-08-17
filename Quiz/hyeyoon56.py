#https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1
# 알라딘 베스트셀러 1위부터 50위까지 책 제목과 가격을 crawling하여 데이터베이스에 저장해보세요.
# db.py : pymysql 임포트 > create 메서드
# 메인py : 리퀘스트/뷰티풀숲/db.py 임포트 > 크롤링 > db.create(data) 호출
import requests
from bs4 import BeautifulSoup


url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1'
doc = requests.get(url)
soup = BeautifulSoup(doc.text, 'html.parser')

a1 = soup.findAll('div', 'ss_book_list')

print(a1)

