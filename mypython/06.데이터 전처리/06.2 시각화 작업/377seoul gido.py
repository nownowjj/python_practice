import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.family'] = 'Malgun Gothic'

filename = 'allStoreModified.csv'
myencoding = 'UTF-8'
mycolor = ['r','g','b','m']
brand_dict = {'cheogajip':'처가집','goobne':'굽네','nene':'네네','palicana':'페리카나'}

myframe = pd.read_csv(filename,encoding=myencoding,index_col=0)
print(myframe.head())

seoulframe = myframe.loc[myframe['sido'] == '서울특별시'] #sido가 서울특별시인것
doframe = myframe.loc[myframe['sido'] == '경기도'] # sido가 경기도인것


newframe = pd.concat([seoulframe,doframe],axis=0)  # 두개 frame concat
print(newframe)

mygrouping = newframe.groupby(['brand'])['brand']
chartdata = mygrouping.count()
chartdata.index = [brand_dict[item] for item in chartdata.index]
print(chartdata)

plt.figure()
chartdata.plot(kind='bar',rot=0,title='서울/경기도 점포 개수',legend=False,color=mycolor,ylim=[0,500],grid=True)
plt.show()