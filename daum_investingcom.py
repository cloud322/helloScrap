#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup



URL = 'https://investing.com/currencies'

#스크래핑 해서 소스를 source_code 에저장
source_code = requests.get(URL)

print(source_code.text)

#텍스트 추출을 위해 lxml 로 테그분석 (메모리 적제)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')






