import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

theaterfile = 'theater.csv'
colnames = ['id','theater','region','bindo']  # 컬럼이 없으므로 만들어줌
dftheaher = pd.read_csv(theaterfile,header=None,names=colnames)

dftheaher = dftheaher.reindex(columns=['id','theater','region','bindo'])

print('대한 배제 후','-'*30)
dftheaher = dftheaher[dftheaher.theater != 'daehan'] # 대한 배제
print(dftheaher)
print('-'*30)

print('sumseries')
newgroup = dftheaher.groupby('id')['bindo'] #영화별 상영빈도
sumseries = newgroup.sum()
print(type(sumseries))
print(sumseries)
print('-'*30)

slice = [sumseries[0],sumseries[1],sumseries[2],sumseries[3]] ## pie x값에 들어갈 값
print(slice)
label = [sumseries.index[0],sumseries.index[1],sumseries.index[2],sumseries.index[3]] # pie label에 추가할 영화별 이름
print(label)

plt.pie(
        x=slice,
        labels=label,
        counterclock=False,
        startangle=90,
        autopct='%1.2f%%'
            )
# plt.show()
plt.title('극장(daehan)을 배제한 영화별 상영 빈도')



filename = 'theaternotpie.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')

#daehan을 배제하고 영화별 상영 건수 파이 그래프로 그려 보세요.
