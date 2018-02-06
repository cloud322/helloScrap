#-*- coding: utf-8 -*-

#python mysql 사용하려면 python 표준 DB API 이용
#MYsql DB  모듈을 다운로드한후 설치해야함 pymySQL

import pymysql

#mysql connection 생성
conn = pymysql.connect(host='192.168.27.128',user='cloud',passwd='Abcdef_12', db='cloud',charset='utf8')


#connection 에서 cursor 생성
curs = conn.cursor()

#sql 문작성후 실행
sql = 'select * from employees'
curs.execute(sql)

#필요하다면 실행한 sql 로부터 데이터 처리
rows = curs.fetchall()
for row in rows:
    print(row[0],row[1],row[2])
    # print(row['lastName'],row['email'],row[]) 안됨

#connection 닫기
curs.close()
conn.close()

#사전식 커서 사용
conn = pymysql.connect(host='192.168.27.128',port=3306,user='cloud',passwd='Abcdef_12', db='cloud',charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = 'select * from customers where state=%s and city=%s'
curs.execute(sql, ('NY', 'NYC'))

rows = curs.fetchall()
for row in rows:
    print(row['phone'], row['city'], row['state'])

curs.close()
conn.close()

#-------간단한 CRUD 테스트
#-------delete from index_test
#-------insert into index_test values ('cloud', '98765')
#-------select * from index_test
#-------update index_test set uid = 'clouddd' where uid ='cloud'
#-------select * from index_test

conn = pymysql.connect(host='192.168.27.128',port=3306,user='cloud',passwd='Abcdef_12', db='cloud',charset='utf8')
curs = conn.cursor()

sql = 'delete from INDEX_test'
curs.execute(sql)

curs.close()
conn.commit()       #insert update delete


##################################################
curs = conn.cursor()
sql = 'insert into INDEX_test values(%s, %s)'
curs.execute(sql, ('abc', '987654'))
conn.commit()
curs.close()

###############################################

curs = conn.cursor()
sql = 'update INDEX_test set uid =%s where uid =%s'
curs.execute(sql, ('xyz', 'abc'))
rows = curs.fetchall()

curs.close()
conn.commit

#############################################조회
curs = conn.cursor(pymysql.cursors.DictCursor)
sql ='select * from INDEX_test'
curs.execute(sql)
rows = curs.fetchall()
for row in rows:
    print(row['uid'], row['pwd'])

curs.close()
conn.close()