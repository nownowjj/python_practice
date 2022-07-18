import pandas as pd

colnames = ['지역','브랜드','매장수']
chickenfile = 'chicken.csv' # 파일 이름
myframe = pd.read_csv(chickenfile,names=colnames,header=None,encoding='UTF-8') # 파일읽기
print(myframe)
print('-'*30)

mygrouping = myframe.groupby('브랜드')['매장수']
print(type(mygrouping)) # type seriesgroupby
print('-'*30)

myseries = mygrouping.sum()
print(myseries)  # 브랜드별 매장수 더한 데이터
print('-'*30)


import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'


mycolor = ['red','green','blue']
mytitle = '브랜드별 매장 개수'
myylim = [0, myseries.max() + 5]
myalpha = 0.7  # 투명도

myseries.plot(kind='bar',color=mycolor,title=mytitle,legend=False,
              rot=0 ,ylim=myylim,alpha=myalpha)
plt.show()
print('finished')
