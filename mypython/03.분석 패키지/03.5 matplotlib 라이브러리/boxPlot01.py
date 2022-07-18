import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = '점수데이터.csv'
myframe = pd.read_csv(filename,encoding='UTF-8', index_col=0)

print(myframe['jumsu'].unique()) # lower upper 구분

frame01 = myframe.loc[myframe['jumsu'] == 'lower','length']
frame01.index.name='lower'
print(frame01.head())  # 5행까지만 한번 체크
print('-'*30)

frame02 = myframe.loc[myframe['jumsu'] == 'upper','length']
frame02.index.name = 'upper'
print(frame02.head())
print('-'*30)

# concat 합침
totalframe = pd.concat([frame01,frame02],axis=1,ignore_index=True)
totalframe.columns = ['lower','upper']
print(totalframe.head())
print('-'*30)

totalframe.plot(kind='box',grid=True)

plt.xlabel('점수 구분')
plt.ylabel('길이')
plt.title('점수에 따른 길이의 상자 수염 그래프')

filename = 'boxPlot01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')
