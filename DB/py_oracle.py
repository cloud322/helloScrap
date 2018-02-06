# -*- coding: utf-8 -*-
import cx_Oracle
import os

# python 에서 oracle 사용하려면
# 먼저 Oracle Instant Client 의 부속파일 설치해야함

# oracle .com 에서 Oracle Instant Client 원도우 x64
# Instant Client basic, Instant Client sqlplus
# c:\JAVA
# 2 visual studio 2013
# 3 환경변수 설정
# ORACLE_HOME, TNS_ADMIN, LD_LIBRARY, Path
# 4 cx_Oracle 모듈 설치

# os.environ['NLS_LANG'] = '.AL32UTF8' # 오라클 환경변수로 인코딩 설정
os.putenv('NLS_LANG', '.AL32UTF8') # 오라클 환경변수로 인코딩 설정

conn = cx_Oracle.connect('hr/hr@192.168.27.128:1521/xe')
print(conn.version)

curs = conn.cursor()
ora = 'select * from employees'
curs.execute(ora)

rows = curs.fetchall()
for row in rows:
    print(row[0],row[1],row[2])
    #오라클에서는 Dict cursor 공식적으로 지원하지 않음

# cols = dict((name,col) for col, name in enumerate(curs.description))
# print(cols['enail',cols['JOB_ID'])

curs.close()
conn.close()





