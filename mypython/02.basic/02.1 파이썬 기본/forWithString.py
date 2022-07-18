mystring = 'life is an egg'

# 스페이를 구분자로 문자열을 나누어 list로 만들어 줍니다
mylist = mystring.split()
print(type(mylist))


for idx in range(len(mylist)): # len = 4  == 0,1,2,3
    if idx %2 == 0 :
        mylist[idx] = mylist[idx].upper()
    else :
        mylist[idx] = mylist[idx].lower()

print('조인 함수 사용하기')
result ='#'.join(mylist)

print(result)
