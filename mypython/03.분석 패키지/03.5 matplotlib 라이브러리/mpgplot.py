import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'mpg.csv'
myframe = pd.read_csv(filename)
print(myframe.head())
print('-'*30)

labels = myframe['drv'].unique()

for item in labels:
    xdata = myframe.loc[myframe['drv'] == item, 'displ']
    ydata = myframe.loc[myframe['drv'] == item, 'hwy']
    plt.plot(xdata,ydata,linestyle='None',marker='o',label=item)

plt.legend(loc=4) #location 줄임말 4는 오른쪽 하단   1 ~4 까지 반시계 방향
plt.xlabel('구동방식(drv) displ')
plt.ylabel('구동방식(drv) hwy')
plt.title('구동방식에 대한 산점도')
plt.grid(True)



filename = 'mpgplot.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')

#구동 방식(drv 컬럼) 별로 displ 컬럼을 x, hwy 컬럼을 y로 하는 산점도 그래프를 그려 보세요.