import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

slices = [1,2,3,4]
hobbies = ['잠자기','외식','영화 감상','운동']
mycolors =['blue','#6AFF00','yellow','#FF00CC']

plt.pie(
    x=slices,
    labels=hobbies,
    colors=mycolors,
    counterclock=False,
    startangle=90,
    autopct='%1.2f%%',
    shadow=True,
    explode=(0,0.1,0,0) # 4가지의 hobbies 중에 2번째에 효과를 줌

    )
#countercolck = 반시계가 기본임
#startangle = 시작 각도 설정
filename = 'pieGraph01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')
