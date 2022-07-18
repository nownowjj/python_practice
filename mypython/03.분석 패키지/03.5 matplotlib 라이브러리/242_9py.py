import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

mycolors=['blue','#6AFF00','yellow','#FF003C','green']
mylist = [30,20,40,60,50]
myindex = ['이상화','한용운','노천명','윤동주','이육사']
# myframe= pd.DataFrame(index=myindex)
# print(myframe)

plt.pie(
    x=mylist,
    labels=myindex,
    colors=mycolors,
    startangle=90,
    autopct='%1.2f%%',
    explode=(0,0.1,0,0,0),
    counterclock=False
    # shadow=5

)
plt.legend(loc=4)
# plt.show()


filename = '242_9py.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')
