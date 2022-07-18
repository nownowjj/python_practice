import numpy as np 
from pandas import DataFrame

myindex = ['이순신', '김유신', '강감찬', '광해군', '연산군']
mycolumns = ['서울', '부산', '광주', '목포', '경주']
mylist = list(10 * onedata for onedata in range(1, 26))
# print(mylist)

myframe = DataFrame(np.reshape(mylist, (5, 5)), index=myindex, columns=mycolumns)
print(myframe)
print('-'*40)

result = myframe.iloc[1]
print(result)
print(type(result))
print('-'*40)

result = myframe.iloc[[1, 3]]
print(type(result))
print(result)
print('-'*40)

result = myframe.iloc[0::2]
print(result)
print('-'*40)

result = myframe.loc['이순신']
print(result)
print('-'*40)

result = myframe.loc[['이순신']]
print(result)
print('-'*40)

result = myframe.loc[['이순신', '강감찬']]
print(result)
print('-'*40)

result = myframe.loc[['강감찬'], ['광주']]
print(result)
print('-'*40)

result = myframe.loc[['연산군', '강감찬'], ['광주', '목포']]
print(result)
print('-'*40)

result = myframe.loc['김유신':'광해군', '광주':'목포']
print(result)
print('-'*40)

result = myframe.loc['김유신':'광해군', ['부산']]
print(result)
print('-'*40)

result = myframe.loc[[False, True, True, False, True]]
print(result)
print('-'*40)

result = myframe.loc[myframe['부산'] <= 100]
print(result)
print('-'*40)

result = myframe.loc[myframe['목포'] == 140]
print(result)
print('-'*40)

# result = myframe.loc[myframe['부산'] >= 70 & myframe['목포'] >= 140]
cond1 = myframe['부산'] >= 70
cond2 = myframe['목포'] >= 140
df = DataFrame([cond1, cond2])
print(df)
print('-'*40)

print(df.all())
print('-'*40)

print(df.any())
print('-'*40)

result = myframe.loc[df.all()]
print(result)
print('-'*40)

result = myframe.loc[lambda df : df['광주'] >= 130]
print(result)
print('-'*40)

myframe.loc[['이순신', '강감찬'], ['부산']] = 30
print(myframe)
print('-'*40)

myframe.loc['김유신':'광해군', ['경주']] = 80
print(myframe)
print('-'*40)

myframe.loc[['연산군'], :] = 50
print(myframe)
print('-'*40)

myframe.loc[:, ['광주']] = 60
print(myframe)
print('-'*40)

myframe.loc[myframe['경주'] <= 60, ['경주', '광주']] = 0
print(myframe)
print('-'*40)
print('-'*40)
print('-'*40)
