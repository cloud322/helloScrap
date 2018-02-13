# -*- coding: utf-8 -*-
import  sys
import codecs



sys.stdin = codecs.open('mapresult.txt','r', 'utf-8')
# 맵 단ㄹ계에서 처리한 결과가 들어 있는 파일을 읽어옴

word2count = {}
# 리듀스한 중간 최종결과를 저장하기위해 dict 자료구조 이용

for line in sys.stdin:  # 파일의 내용을 한줄씩 읽어서
    cline = line.strip()    #라인의 앞뒤 공백 제거
    word, count = cline.split('\t', 1)  # 탭과 구분해서 2개의 항목으로 분리 각가을 word count 에 저장

    try:
        count = int(count)      # 문자값인 count 숫자로 변환
    except ValueError:
        continue                # 오류 공백발생시 무시
        # count = int(0)

    try:
        word2count[word] = word2count[word] + count
        # dict 자료구조에 문자와 빈도를 저장
        # 문자는 키로 출현빈도는 값형태로 처리
        # 만일 기존에 저장된 문자가 있다면 그문자의 출현빈도에 합산처리
    except:
        word2count[word] = count
        # dict 자료구조에 문자와 출현 빈도를 저장할때
        # 오류가 발생하면 문자,출현빈도는 키와 값으로 저장
        # 문자키로 검색했는 데 값이 존재 하지 않으므로

    print(word2count)
    # 리듀스 중간처리 결과 확인

for word in word2count.keys():
    # word2count에 저장된 모든 키를 하나씩 읽어와서
    print('%s\t%s' % (word, word2count[word]))
    # 그키에 해당하는 값을 출력