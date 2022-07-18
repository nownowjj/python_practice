import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'ex802.csv'
myframe = pd.read_csv(filename,index_col='type',encoding='UTF-8')
myframe.index.name = '자동차 유형'
myframe.columns.name = '도시(city)'

print(myframe)
print('-'*30)

myframe.plot(kind='bar',rot=0 ,title='차량 유형별 지역별 등록 대수',legend=True)

filename = 'DataframeGraph02_01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')

myframeT=myframe.T

myframeT.plot(kind='bar',rot=0 ,title='지역별 차량 등록 대수',legend=True)
filename = 'DataframeGraph02_02.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')

ymax = myframeT.sum(axis=1).max()+50
print(ymax) # 지역별 총합중에서 제일 큰것

myframeT.plot(kind='bar',rot=0 ,title='지역별 차량 등록 대수',legend=True ,stacked=True,ylim=[0,ymax])
filename = 'DataframeGraph02_03.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')
