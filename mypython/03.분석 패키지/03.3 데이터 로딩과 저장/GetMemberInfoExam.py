import pandas as pd

filename = 'data02.csv'
myframe = pd.read_csv(filename, index_col=0, header=None, names=['학년', '국어', '영어', '수학'])

myframe.index.name = '이름'

myframe.loc[['강호민'], ['영어']] = 40
myframe.loc[['박영희'], ['국어']] = 30

print(myframe)
print('-'*30)

# astype : 컬럼의 타입 변경
df = myframe.astype({"영어": int}, errors='raise')
print(df)
print('-'*30)




