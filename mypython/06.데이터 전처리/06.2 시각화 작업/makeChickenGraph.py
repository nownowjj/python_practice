import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

chickenfile = 'allStoreModified.csv' # 파일 이름
myframe = pd.read_csv(chickenfile,encoding='UTF-8',index_col=0) # 파일읽기
print(myframe.head())
print('-'*30)

print(myframe['brand'].unique()) # 매장 종류
print('-'*30)

mycolor = ['r','g','b','m']
brand_dict = {'cheogajip':'처가집','goobne':'굽네','nene':'네네','palicana':'페리카나'}

mygrouping = myframe.groupby('brand')['brand']

chartdata =mygrouping.count()

        # ex nene가 네네가 됨           /가게명 순서대로
newindex = [brand_dict[idx] for idx in chartdata.index]
#newindex = 처가집,굽네,네네,페리카나

#chartdata의 index를 newindex로 변경
chartdata.index = newindex
print(chartdata) #확인
print('-'*30)

plt.figure() # 새 도화지 준비

chartdata.plot(kind='pie',legend=False,autopct='%1.2f%%',colors=mycolor,rot=0)
filename = 'makeChickenGraph01.png'
plt.savefig(filename)
print(filename ,'파일 저장됨')


plt.figure()
chartdata.plot(kind='bar',legend=False,color=mycolor,rot=0,title='브랜드별 매장 개수')
filename = 'makeChickenGraph02.png'
plt.savefig(filename)
print(filename ,'파일 저장됨')


print('finished')
