import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

theaterfile = 'theater.csv'
colnames = ['id','theater','region','bindo']  # 컬럼이 없으므로 만들어줌
dftheaher = pd.read_csv(theaterfile,header=None,names=colnames)

dftheaher = dftheaher.rename(index=dftheaher.id) # 기존 색인 0,1,2를 id값으로 치환
dftheaher = dftheaher.reindex(columns=['theater','region','bindo'])
# 색인 0,1,2를 id값으로 치환함 , column에서 id를 제외
dftheaher.index.name = 'id' # 색인에 이름 매김
print(dftheaher.head())

print('극장별 상영 집계 횟수') # db에선 극장별로 bindo를 더하려면 group by를 써야함
                        # theater로 그룹으로 묶어라
mygrouping = dftheaher.groupby('theater')['bindo']
sumseries = mygrouping.sum()   # 극장별 빈도의 총합
print(sumseries)

meanseries =mygrouping.mean()  # 극장별 빈도의 평균
print(meanseries)

sizeseries = mygrouping.size() # 극장별 수
print(sizeseries)

df = pd.concat([sumseries,meanseries,sizeseries],axis=1)
df.columns=['합계','평균','개수']
print(df)

mysize = len(mygrouping.groups) #그룹 수

df.plot(kind='barh',rot=0)
plt.title(str(mysize) + '개 매장 집계 데이터')



filename = 'visualizationExam_01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')

print('집계 메소드를 사전에 담아 전달하기')
print('지역의 개수와 상영회수의 총합')

# agg는 aggregate의 줄임말
mydict = {'bindo':['sum','mean'],'region':'size'}
    # bindo의  합과 평균  --     극장별  사이즈
result = dftheaher.groupby('theater').agg(mydict)
print(result)
print('-'*30)

print('numpy를 이용한 방법')
result = mygrouping.agg([np.count_nonzero,np.mean,np.std])
print(result)
print('-'*30)

from math import sqrt

def myroot(values):
    # 총합에 root 씌워서 리턴
    mysum = sum(values)
    return sqrt(mysum)

def plus_add(values,somevalue):
    #총합에 root 씌워서 somevalue를 더해 주는 함수
    result = myroot(values) + somevalue
    return result

mygrouping = dftheaher.groupby('theater')['bindo']
print('groupby와 사용자 정의 함수 같이 쓰기')
result = mygrouping.agg(myroot)
print(result)
print('-'*30)

print('groupby와 사용자 정의 함수(매개 변수 2개) 같이 쓰기')
result = mygrouping.agg(plus_add,somevalue=3)
print(result)
print('-'*30)

print('컬럼 2개 이상을 그룹화 하기')
newgrouping = dftheaher.groupby(['theater','region'])['bindo']
result = newgrouping.count()
print(result)
print('-'*30)

