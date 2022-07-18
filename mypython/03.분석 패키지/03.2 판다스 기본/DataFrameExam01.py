from pandas import DataFrame

sdata = {
            '도시':['서울', '서울', '서울', '부산', '부산'],
            '년도':[2000, 2001, 2002, 2001, 2002],
            '실적':[150, 170, 360, 240, 290],
        }

myindex = ['one', 'two', 'three', 'four', 'five']
myframe = DataFrame(sdata, index=myindex)
print(myframe)
print(type(myframe))

myframe.columns.name = '하하하'

myframe.index.name = '호호호'

print(myframe.index)

print(myframe.columns)

print(type(myframe.values))
print(myframe.values)

print(myframe.dtypes)

print(myframe.T)

print(myframe)

mycolumns = ['실적', '도시', '년도']
newframe = DataFrame(sdata, columns=mycolumns)
print(newframe)

