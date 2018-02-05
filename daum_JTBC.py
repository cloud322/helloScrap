#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

#다음 JTBC 뉴스 스크래핑 예제
# http://media.daum.net/cp/310
# ?page=2&cateId=1001&regDate=20180205

press = [310]
date = [20180205]
page = [1,2,3]

news_title =[]
news_desc = []

URL = 'http://media.daum.net/cp/' +str(press[0])+ '?page=' + str(page[0]) + '&regDate=' + str(date[0])

#스크래핑 해서 소스를 source_code 에저장
source_code = requests.get(URL)

#print(source_code.text)

#텍스트 추출을 위해 lxml 로 테그분석 (메모리 적제)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')

#기사제목추출
cnt=1
for title in soup.select("a['class=link_txt']"):
    if cnt > 15:break
    #print(title.text.strip())
    news_title.append(title.text.strip())
    cnt+=1

#기사간단소개 추출

cnt=1
for title in soup.select("span['class=link_txt']"):
    if cnt > 15:break
    #print(title)
    news_desc.append(title.text.strip())
    cnt+=1


for i in range(0,15):
    print(news_title[i])
    print('%s\n'% news_desc[i])








