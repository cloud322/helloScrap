# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://kr.investing.com/currencies/'

driver = webdriver.Firefox(executable_path = r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get(URL)
# 페이지 오른쪽 암호화페탭의 xpath 정의
# //*[@id="QBS_7"]                                       # * 모든
# /html/body/div[5]/aside/div[2]/div[1]/ul/li[4]/a       # a href ='' 암호화폐
alink = driver.find_element_by_xpath('//li[@id="QBS_7"]/a')

# 마우스 단축키 이벤트, 처리를 위해 ActionChains 초기화
mouse =webdriver.ActionChains(driver)

# 해당링크를 마우스 클릭으로 처리하기 위해 move_to_element 사용
mouse.move_to_element(alink).click().perform()

# 클릭후 보여지는 페이지 내용을 source_code 에저장후 출력
source_code = driver.page_source
#print(source_code)

# 웹페이지 내용을 parsing 하기 위해 bs4로 초기화
soup = BeautifulSoup(source_code, 'html.parser')

crypcurr = ['btc-usd','btc-krw','eth-usd']
crypval = ['945629', '940808', '997650']


## currid=("data-gae=-btc-usd","data-gae=-btc-krw", "data-gae=-eth-usd","data-gae=-bch-krw", "data-gae=-iot-usd")

#종류 data-gae="-btc-usd"
#가격 id="sb_last_945629"
for i in range (0, len(crypcurr)):
    findkey = 'a["data-gae=-'+ crypcurr[i] +'"]'
    for title in soup.select(findkey):
        print(title.text)
        #print((title.text).encode('utf-8'))
        #movie_rank.append(" ".join(title.text.strip().split()))


    findkey = 'td["id=sb_last_'+ str(crypval[i]) +'"]'
    for title in soup.select(findkey):
        print(title.text)

#browser닫기
driver.close()
