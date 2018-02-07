# -*- coding: utf-8 -*-
from scrapy import cmdline
# scrapy 원도우 상에서 구동하려면  pycharm 환경 설정에서 cmdline.execute() 메서드 이용
# 먼저 pycharm 환경에 scrapy가 설치 잇어야 단 추가설치패키지는 pypiwin32
cmdline.execute("scrapy runspider currencySpider.py".split())
