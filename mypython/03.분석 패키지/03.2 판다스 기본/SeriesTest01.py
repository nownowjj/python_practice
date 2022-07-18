from pandas import Series

mylist = [10, 40, 30, 20]
myseries = Series(data=mylist, index=['강감찬', '이순신', '김유신', '광해군'])
print(type(myseries))

print(myseries)
print('-'*30)

myseries.index.name = '점수' # 색인의 이름
print(myseries)
print('-'*30)

myseries.name = '학생들 점수' # 시리즈의 이름
print(myseries)
print('-'*30)

print(myseries.index)
print('-'*30)

print(myseries.values)
print('-'*30)

for idx in myseries.index :
    print('색인 : ' + idx, ', 값 : '+ str(myseries[idx]))

