# -*- coding: utf-8 -*-
import scrapy
import codecs
import sys
#리눅스상에서 utf-8 로 파일에 내용을 기록하려면 시스템 기본 인코딩으 ㄹutf-8 로 설정해야함
reload(sys)
sys.setdefaultencoding('utf8')


# scrapy 에서 spider 는 crawling/scrapping을 담당하는 핵심부분
#crawling/scrapping 절차에 대한 정의를 하는 부분
class CurrSpider(scrapy.Spider):
    name = 'currSpider'
    start_urls = ['http://finance.naver.com/marketindex/?tabSel=exchange#tab_section']

    def parse(self, response):

        ranks = response.css('span.blind::text').extract()

        titles = response.css('span.value::text').extract()


        with codecs.open('curr.csv','w','utf-8') as f:
            # 처리결과 저장하기위해
            # movierank.csv 라는 이름으로 쓰기 모드로 open

            # for i in range(0,4):
            #     rank = ranks[i].replace('\r\n', ' ')
            #     rank = ''.join(rank.split())
                print(ranks)

                # title = titles[i].replace('\r\n', ' ')
                # title = title.strip().encode('utf-8')
                print(titles)

                f.write('%s,%s\n' % (ranks, titles))

        f.close()