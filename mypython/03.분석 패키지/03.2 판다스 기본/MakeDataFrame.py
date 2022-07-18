import numpy as np
from pandas import DataFrame

mydata = np.arange(9).reshape((3, 3))
print(mydata)

myframe = DataFrame(data=mydata, index=['용산구', '마포구', '은평구'], columns=['철수', '영희', '바둑이'])
print(myframe)

sdata = {'지역':['용산구', '마포구'], '년도':[2019, 2020]}
myframe = DataFrame(data=sdata)
print(myframe)

sdata = {'용산구': {2020:10, 2021:20}, '마포구':{2020:30, 2021:40, 2022:50}}
myframe = DataFrame(data=sdata)
print(myframe)

sdata = {
            '지역':['용산구', '용산구', '용산구', '마포구', '마포구'],
            '년도':[2019, 2020, 2021, 2020, 2021],
            '실적':[20, 30, 35, 45, 55]
        }
myframe = DataFrame(data=sdata)
print(myframe)











