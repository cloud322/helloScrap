# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#selenium 설치
# firefox 용 webdriver 다운


noWrap_list = []   # 순위
pid_list = []  # 제목

URL = 'https://kr.investing.com/currencies/'

# firefox 를 띄워 browser 에 나타난 source scraping
driver = webdriver.Firefox(executable_path = r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
#웹브라우저르 ㄹ자동화할 수 있도록 특수하게 컴파일된 브라우저인 geckodriver을 다운로드 후 지정한 위치에 저장

# 스크래핑해서 소스를 에 저장
#source_code = requests.get(URL)
driver.get(URL)
source_code = driver.page_source    #firefox 에서 가저온 소스를 source_code변수에저장

# print(source_code)
soup = BeautifulSoup(source_code, 'lxml')          #  xml 파서(분석기)

currid=(1,2,3,125,5,6,7,8,650,159)

# 순위 추출

findkey = 'td["class=left noWrap"]'
for title in soup.select(findkey):
    print(title.text.strip().split())
    #movie_rank.append(" ".join(title.text.strip().split()))


# 제목 추출
for i in range (0, len(currid)):
    findkey = 'td["class=pid-"'+str(currid[i])+'"-last"]'
    for title in soup.select(findkey):
        print(title.text.strip().split())

