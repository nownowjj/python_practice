tuple01 = (10,20,30)
tuple01 = tuple01 + (40,)
print(tuple01)

tuple02 = 10,20,30,40
print(type(tuple02))

mylist = [10,20,30,40]
tuple03 = tuple(mylist)

if tuple02 == tuple03 :
    print('equal')
else :
    print('no equal')

tuple04 = (10,20,30)
tuple05 = (40,50,60)

print('+ 기호는 듀플을 합쳐 줍니다.')
tuple06 = tuple04 + tuple05
print(tuple06)

print('* 기호는 듀플을 지정한 수만큼 반복시킵니다.')
tuple07 = tuple04 * 5
print(tuple07)

print('swap 기법')
a,b=11,22
a,b= b,a
print(a,b)

tuple08 = (11,22,33,44,55,66)
print(tuple08[1:3])

print(tuple08[3:])

tuple08[4] = 100