import re

mylist = ['ab123','cd4#6','cf79a','abc1']

# a또는 c로 시작하고, 이후 숫자또는 알파벳이 4개로 끝나는 항목
regex = '[ac]{1}[0-9a-z]{4}'
    # a또는 c 1개  , 숫자또는 알파벳 4개
pattern = re.compile(regex)

totallist = []
totallist2 = []

for item in mylist:
    if(pattern.match(item)):
        print(item,'은 조건에 적합')
        totallist.append(item)
    else :
        print(item,'은 조건에 부적합')
        totallist2.append(item)

print('적합한 열',totallist)
print('부적합한 열',totallist2)