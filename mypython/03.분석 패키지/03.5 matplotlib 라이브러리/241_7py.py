import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename= 'mygraph.csv'
myframe = pd.read_csv(filename,index_col='이름',encoding='UTF-8')
myframe.index.name='이름'
myframe.columns.name= '시험 과목'
print(myframe)
print('-'*30)

myframe.plot(kind='bar',rot=0,title='학생별 누적 시험 점수',stacked=True)

filename = 'mygraph.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')
