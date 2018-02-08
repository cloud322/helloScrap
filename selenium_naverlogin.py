# -*- coding: utf-8 -*-
import time
from bs4 import BeautifulSoup
from selenium import webdriver

#포탈 사이트에 로그인한 후 자신이 받은 메일수 확인
URL = 'https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fwww.naver.com'

driver = webdriver.Firefox(executable_path = r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get(URL)

# 로그인창에 아이디 비번 입력후 로그인 버튼클릭
# html 요소 중 id 가 id 인 요소를 찾음
userid = driver.find_element_by_id('id')
# @id = id 인 요소에 아이디 입력
userid.send_keys('123123123')

userpw = driver.find_element_by_id('pw')
# @id = id 인 요소에 아이디 입력
userpw.send_keys('123123123')
2

# 로그인버튼을 찾아 클릭
loginbtn = driver.find_element_by_xpath('//input[@title="Sign in"]')
loginbtn.submit()

#처리속도가 빨라서 로그인완료페이지뜨기전에 메일확인 페이지로 이동

#따라서 로그인완료페이지가 뜨는걸 확인하기 위해 (서버로부터 넘어오는 응답데이터를 다받을떆까지
#일정시간동안 브라우저 잠시 대기시킴
#driver.implicitly_wait(3)
time.sleep(3)


#메일페이지 이동
MailURL = 'http://mail.naver.com/login?url=http%3A%2F%2Fmail.naver.com%2F'
driver.get(MailURL)

source_code = driver.page_source
soup = BeautifulSoup(source_code, 'html.parser')
# 안읽은 메일확인(span id="headUnreadNum"  span[class=cnt])
findkey = 'span["class=cnt"]'
for title in soup.select(findkey):
    print(title.text.strip())

#logout
time.sleep(3)
mouse =webdriver.ActionChains(driver)
# logoutbtn = driver.find_element_by_id("//*[@id='gnb_name1']")
# mouse.move_to_element(logoutbtn).click().perform()
#
# time.sleep(3)
#
# mouse =webdriver.ActionChains(driver)
# logoutbtn = driver.find_element_by_id("gnb_logout_button")
# mouse.move_to_element(logoutbtn).click().perform()

time.sleep(3)
driver.get('https://nid.naver.com/nidlogin.logout?')
