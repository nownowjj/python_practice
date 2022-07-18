import pandas as pd
from pandas import DataFrame

myencoding = 'utf-8'
chickenList = ['cheogajip','goobne','nene','palicana'] # 치킨 리스트

newframe = DataFrame()
print(newframe)
print('-'*30)

for onestore in chickenList:
    filename = './data/' + onestore + '.csv' # 매장별 csv 파일 경로 설정
    print(filename)                 # 확인 해보기
    myframe = pd.read_csv(filename,index_col=0,encoding=myencoding) # 리스트 순서대로 프레임 생성
    newframe = pd.concat([newframe,myframe],axis=0,ignore_index=True) # 리스트 4개 concat
    print(myframe.head())   # 매장별 5개씩만 출력해보기
# end for

print(newframe.info())      # concat 시킨 frame info
print('-'*30)

totalfile = 'allstore.csv'     # concat frame을 저장할 이름
newframe.to_csv(totalfile,encoding=myencoding) # csv파일로 만들기 
print(totalfile+'파일 저장 완료')