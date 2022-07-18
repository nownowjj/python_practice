from urllib.request import urlopen
from bs4 import BeautifulSoup

myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
myresponse= urlopen(myurl)
soup=BeautifulSoup(myresponse,myparser)
# print(soup)

#  d:드라이브 imsi\월요일
import os

# 월~일 사전 생성
weekday_dict = {'mon':'월요일','tue':'화요일','wed':'수요일','thu':'목요일','fri':'금요일','sat':'토요일','sun':'일요일'}
#저장할 폴더 경로
myfolder = "d:\\imsi\\" # 임시폴더

try :
    if not os.path.exists(myfolder) :  # 운영체제에 이 폴더가 존재하지 않으면
        os.mkdir(myfolder)  # 마이폴더를 생성

    for mydir in weekday_dict.values():
        mypath = myfolder + mydir
        # print(mypath)
        if os.path.exists(mypath):
            pass
        else:
            os.mkdir(mypath)


except FileExistsError as err :
    pass # 오류 무시하고 통과


def saveFile(mysrc,myweekday,mytitle):
    image_file = urlopen(mysrc)
    filename = myfolder + myweekday + '\\' + mytitle +'.jpg'
    # print(filename)
    myfile = open(filename,mode='wb')
    myfile.write(image_file.read()) # 바이너리로 저장
#end def saveFile



mytarget = soup.find_all('div',attrs={'class':'thumb'})
print('카툰 총 개수 : %d' % (len(mytarget)))
print(mytarget)

mylist = [] # 데이터를 저장할 리스트

for abcd in mytarget:
    myhref = abcd.find('a').attrs['href'] #div class가 thumb인 a태그
    myhref=myhref.replace('/webtoon/list?','') #공백으로 치환
    print(myhref) # ex : titleId=783599&weekday=sun

    result = myhref.split('&') #split으로 나누면 list에 담김
    mytitleid= result[0].split('=')[1]
    myweekday =result[1].split('=')[1]
    myweekday =weekday_dict[myweekday]

    # print(mytitleid + '/' + myweekday)

    imgtag = abcd.find('img')
    mysrc = imgtag.attrs['src']
    mytitle = imgtag.attrs['title']
    mytitle= mytitle.replace('?','').replace('/','').replace(':','') # ?가 있으면 공백으로
    # print(mytitle + '/' + mysrc)

    saveFile(mysrc,myweekday,mytitle)

    mytuple = tuple([mytitleid,myweekday,mytitle,mysrc])
    mylist.append(mytuple)
#end for

# print(mylist)

from pandas import DataFrame


filename='cartoon.csv'
myframe =DataFrame(mylist,columns=['타이틀 번호','요일','제목','링크'])
myframe.to_csv(filename,encoding='UTF-8',index=False)

print(filename + '파일 저장')
print('finished')