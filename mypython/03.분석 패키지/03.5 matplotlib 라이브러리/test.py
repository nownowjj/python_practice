import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'tips.csv'
myframe = pd.read_csv(filename,encoding='UTF-8')

mycolors =['r','b']
labels = myframe['sex'].unique() # male female
cnt = 0
# tips.csv에서 첫번째 성별은 female임 그럼 female이 red로 먼저 실행
for item in labels: # 성별 male ,female로 반복문을 2번실행
    xdata = myframe.loc[myframe['sex'] == item,'total_bill']
    ydata = myframe.loc[myframe['sex'] == item,'tip']
    plt.plot(xdata,ydata,color=mycolors[cnt],marker='o',linestyle='None',label=item)
#      x축은 결재총액, y축은 팁
    cnt +=1

plt.legend()
plt.xlabel('결재 총액')
plt.ylabel('팁 비용')
plt.title('결재 총액과 팁 비용의 산점도')
plt.grid(True)

filename = 'test.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')
