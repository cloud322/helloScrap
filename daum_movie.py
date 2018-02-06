#-*- coding: utf-8 -*-
import codecs

import requests
from bs4 import BeautifulSoup

#영화순위

# 순위 : info_poster >num_rank
# 제목 : tit_poster > link_txt


#http://movie.daum.net/main/new#slide-1-0


movie_rank =[]
movie_title = []
movie_grade = []
movie_opdate = []

URL = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'
source_code = requests.get(URL)

#print(source_code.text)

plain_text = source_code.text
# soup = BeautifulSoup(plain_text, 'html.parser')
soup = BeautifulSoup(plain_text, 'lxml')

#print(soup)

#rank
for i in range(1, 21):
    findkey = 'span["class=ico_ranking ico_top'+str(i)+'"]'
    for title in soup.select(findkey):
        #print(" ".join(title.text.strip().split()))
        movie_rank.append(" ".join(title.text.strip().split()))
#title
findkey = 'a["class=link_g"]'
for title in soup.select(findkey):
    #print(title.text.strip())
    movie_title.append(title.text.strip())

#평점
findkey = 'em["class=emph_grade"]'
for title in soup.select(findkey):
    #print(title.text.strip()) + "/10"
    movie_grade.append(title.text.strip())

#개봉일
findkey = 'dl["class=list_state"]'
for title in soup.select(findkey):
    #print(title.select('dd')[0].text)
    movie_opdate.append(title.select('dd')[0].text)


#출력
for i in range(0,20):
    print(movie_rank[i])
    print(movie_title[i])
    print(movie_grade[i])
    print("%s\n" % movie_opdate[i])

#--------파일 저장하기
fmt = '%s,%s,%s,%s\n'   #출력형식 정의
f = open('movie_rank2','w')         #파일을 쓰기모드로 open
# f.write('hello,python\n')           #파일에 내용쓰기
# f.write('ㅎㅇㅎㅇㅎㅇ안녕\n')             #파일 작업 종료
for i in range(0,20):
    rank = fmt % (movie_rank[i], movie_title[i], movie_grade[i], movie_opdate[i])
    #f.write(rank)      #오류 유니코드문자 저장시  - codes 추천
    #python 2 기본적으로 모든문자 ASCII
    #파일 기록시 먼저 ASCII 디코딩하기 때문 오류

f.close()               #파일 작업 종료 필수!

f = codecs.open('movie_rank2a.txt','w','utf-8')
for i in range(0,20):
    rank = fmt % (movie_rank[i], movie_title[i], movie_grade[i], movie_opdate[i])
    f.write(rank)
f.close()

#--------파일 저장하기 3.5
#readLine   : 한줄씩 읽어옴 (추가적으로 while 필요)
#readLines  : 모둔줄을 list로 읽어옴 (추가적으로 for 필요)
#read       : 파일 내용 전체 읽어



try:
    f = open('movie_rank2b.txt','w',encoding='utf-8')
    for i in range(0,20):
        rank = fmt % (movie_rank[i], movie_title[i], movie_grade[i], movie_opdate[i])
        f.write(rank)
    f.close()
except Exception as ex:
    print(ex)

#--------파일 읽어 출력 2
f = codecs.open('movie_rank2a.txt','r','utf-8')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()

f = codecs.open('movie_rank2a.txt','r','utf-8')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = codecs.open('movie_rank2a.txt','r','utf-8')
data = f.read()
print(data)
f.close()






#--------파일 읽어 출력 3
f = open('movie_rank2b.txt','r',encoding='utf-8')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()

f = open('movie_rank2b.txt','r',encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open('movie_rank2b.txt','r',encoding='utf-8')
data = f.read()
print(data)
f.close()

#with ~as 구문으로 파일다루기
#파일 작업시 파일을 열고 닫는 것은 번거로운 일임
#python 알아서 닫아주면 어떨까 - 편리
with open('movie_rank2b.txt','r',encoding='utf-8') as f:
    data =f.read()
    print(data)

#파일 읽기 쓰기 모드
#r ead
#w rite
#t ext
#b inary (img)
#a ppend
#+ update
#파일모드의 기본값은 : rt