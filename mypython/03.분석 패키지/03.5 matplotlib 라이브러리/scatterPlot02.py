import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = '프로야구타자순위2021년.csv'
myframe = pd.read_csv(filename,encoding='UTF-8')
print(myframe.head())  # head(행 수)
print('-'*30)

print(myframe.info())
print('-'*30)

print(myframe['팀명'].unique())
print('-'*30)

mycolors = ['r','g','b']
labels = ['두산','LG','키움'] # list 형식
cnt = 0 # 인덱스 -반복문안에서 숫자 증가 시켜야함

for finditem in labels: # finditem은 두산 lg 키움
    xdata = myframe.loc[myframe['팀명'] == finditem,'안타'] # 0번째는 두산의 안타
    ydata = myframe.loc[myframe['팀명'] == finditem,'타점'] # 0번째는 두산의 타점
    plt.plot(xdata,ydata,color=mycolors[cnt], linestyle='None',marker='o',label=finditem)
    cnt +=1  # 반복문 돌때마다 cnt 1씩증가

plt.legend(loc=4) #location 줄임말 4는 오른쪽 하단   1 ~4 까지 반시계 방향
plt.xlabel('안타 개수')
plt.ylabel('타점')
plt.title('안타와 타점에 대한 산점도')
plt.grid(True)


filename = 'scatterPlot02.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')
