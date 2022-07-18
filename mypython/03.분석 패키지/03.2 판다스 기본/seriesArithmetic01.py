from pandas import Series

myindex1 = ['강호동', '유재석', '김제동', '신동엽']
mylist1 = [30, 40, 50, 60]

myseries1 = Series(data=mylist1, index=myindex1)

myindex2 = ['강호동', '유재석', '김제동', '이수근']
mylist2 = [20, 40, 60, 70]

myseries2 = Series(data=mylist2, index=myindex2)

print(myseries1)
print('-' * 30)

print(myseries2)
print('-' * 30)

print(myseries1 + 5)
print('-' * 30)

print(myseries1.add(5))  # sub, mul, div, floordiv
print('-' * 30)

print(myseries1 >= 40)
print('-' * 30)

newseries = myseries1 + myseries2
print(newseries)
print('-' * 30)

newseries = myseries1.sub(myseries2, fill_value = 0)
print(newseries)
print('-' * 30)
