import os.path
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

myparser = 'html.parser'
myurl = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
myresponse= urlopen(myurl)
soup=BeautifulSoup(myresponse,myparser)
# print(soup)

import os

myfolder = "d:\\movie\\" # 폴더 생성 경로

try :
    if not os.path.exists(myfolder) : # 이 폴더가 없으면
        os.mkdir(myfolder) #폴더 생성

except FileExistsError as err:
    pass # 무시하고 통과

mytrs = soup.find_all('tr')   # 모든 tr을 찾음
# print(mytrs)
no =0               # 순위 변수
totallist =[]       # 값을 담을 리스트
title = ''          # 제목
up_down = ''        # 변동값


#-----------------------------------------------------
#-----------------------------------------------------
for one_tr in mytrs:  # 모든 tr로 반복문 돌림

    mytd = one_tr.find('td',attrs={'class':'title'})  # 모든 tr에서 title class를 가진 td가 있으면 반복문 실행 그렇지 않은 tr은 실행하지 않음
    if(mytd != None):
        no +=1              # 반복문 실행시 no 1씩 증가
        newno = str(no).zfill(2)    # newno에 저장 zfill 두자리 ex 00

        # -------------------------------------
        mytag = mytd.find('div',attrs={'class':'tit3'}) # div class tit3에 a 태그에 문자열
        title = mytag.a.string                          # 제목 저장
        # print(title)
        # -------------------------------------
        mytd =one_tr.select_one('td:nth-of-type(3)')    #tr에 3번째 td는 alt 값에 (na,up,down) 이 존재함
        myimg = mytd.find('img')                #3번째 td에서 img 태그를 찾음
        if myimg.attrs['alt'] == 'up':          # alt값이 up이면 상승
            up_down ='상승'
        elif myimg.attrs['alt'] =='down':       # alt값이 down이면 강등
            up_down ='강등'
        else:
            up_down='불변'                      # alt값이 na이면 불변
        # print(up_down)
        # -------------------------------------
        change = one_tr.find('td',attrs={'class':'range ac'})  # tr에 range ac class를 가진 td를 찾음
        if change == None:                                     # 값이 0이면 None
            pass
        else:                                                  # 값이 존재하면 그 값 그대로 사용
            change=change.string
        # -------------------------------------
        #     print(newno + '/' + title + '/' + up_down +'/' + change)  # 확인 해보고
            totallist.append((newno,title,up_down,change))      # totallist에 append 시킴
#end for
#-----------------------------------------------------
#-----------------------------------------------------
print('-'*30)
print(totallist)

mycolumns = ['순위','제목','변동','변동값']      # 컬럼명 생성
myframe = DataFrame(totallist,columns=mycolumns)        #DataFrame 생성 값: totallist , column = 생성한 컬럼
filename = 'naverMoive.csv'                             #임의에 파일명 생성
myframe.to_csv(filename,encoding='UTF-8',index=False)   #csv파일로 저장
print(filename+'으로 저장되었습니다.')
#순위 제목 변동 변동값


















