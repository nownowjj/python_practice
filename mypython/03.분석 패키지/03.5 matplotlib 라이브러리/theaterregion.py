import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

theaterfile = 'theater.csv'
colnames = ['id','theater','region','bindo']  # 컬럼이 없으므로 만들어줌
dftheaher = pd.read_csv(theaterfile,header=None,names=colnames)

dftheaher = dftheaher.rename(index=dftheaher.id) # 기존 색인 0,1,2를 id값으로 치환
dftheaher = dftheaher.reindex(columns=['theater','region','bindo'])
dftheaher.index.name = 'id' # 색인에 이름 매김

print(dftheaher)
print('-'*30)

mygrouping = dftheaher.groupby('region')['bindo']
sumseries = mygrouping.sum()
print(sumseries)  # 지역별 상영건수 총합
print('-'*30)

sumseries.plot(kind='bar',rot=0,grid=True,ylim=(0,sumseries.max()))
plt.title('지역별 상영건수의 총합')
plt.show()




# filename = 'theaterregion.png'
# plt.savefig(filename, dpi=400)
# print(filename + ' 파일 저장')

#지역별 상영 건수를 막대 그래프로 그려 보세요.
