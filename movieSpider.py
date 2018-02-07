# -*- coding: utf-8 -*-
import scrapy
import codecs

import sys
#리눅스상에서 utf-8 로 파일에 내용을 기록하려면 시스템 기본 인코딩으 ㄹutf-8 로 설정해야함
reload(sys)
sys.setdefaultencoding('utf8')


# scrapy 에서 spider 는 crawling/scrapping을 담당하는 핵심부분
#crawling/scrapping 절차에 대한 정의를 하는 부분
class MovieSpider(scrapy.Spider):
    name = 'movieSpider'
    start_urls = ['http://ticket2.movie.daum.net/Movie/MovieRankList.aspx']
                    #scrap 할 URL

    def parse(self, response):
        #start_url 에 정의된 URL 스파이더가 scrap
        #내용이 다운로두된후 호풀되는 메서드
        #parse()는 실제 추출할 데이터를 작업한 후 결과로 return

        ranks = response.css('.ico_ranking::text').extract()
        #css 선택자를 이용해서 클래스가 ico_ranking인 모든 항목 추출 rank 변수에 저장

        titles = response.css('.link_g::text').extract()
        # css 선택자를 이용해서 클래스가 link_g인 모든 항목 추출 rank 변수에 저장

        with codecs.open('movierank.csv','w','utf-8') as f:
            # 처리결과 저장하기위해
            # movierank.csv 라는 이름으로 쓰기 모드로 open

            for i in range(0,20):
                rank = ranks[i].replace('\r\n', ' ')   #/r/n ->whitespace
                rank = ''.join(rank.split())          #빈칸 으로 분리호 다시 합침
                print(rank)

                #title = titles[i].replace("\r\n", " ")
                #print(title.encode('utf-8'))
                #title = ''.join(title.split())
                title = titles[i].replace('\r\n', ' ')
                title = title.strip().encode('utf-8')
                print(title)

                f.write('%s,%s\n' % (rank, title))
                #순위와 제목을 파일에 기록
        f.close()