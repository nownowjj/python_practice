import pandas as pd

filename = 'memberInfo.csv'
myframe = pd.read_csv(filename)
print(type(myframe))
print(myframe)
print('-'*30)

newdf01 = myframe.set_index(keys=['id'])
print(newdf01)
print('-'*30)

newdf02 = myframe.set_index(keys=['id'], drop=False)
print(newdf02)
print('-'*30)

myframe2 = pd.read_csv(filename, index_col='id')
print(myframe2)
print('-'*30)

filename='memberInfo2.csv'
# header=None 는 컬럼에 대한 헤더가 없습니다.
myframe2 = pd.read_csv(filename, header=None, names=['id', '국어', '영어'])
print(myframe2)
print('-'*30)
















