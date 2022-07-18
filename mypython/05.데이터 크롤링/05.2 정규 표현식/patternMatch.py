import re

# 소문자2개 , 그리고 숫자 3개로 구성된 항목 찾기
mylist = ['ab123','cd456','ef789','abc12']
                    # 마지막 abc12는 조건에 부합하지 않음 = None
regex = '[a-z]{2}\d{3}' # 소문자 2개 숫자 3개

pattern = re.compile(regex)

totallist = [] # 조건에 맞는 항목들만 채워 넣기

for item in mylist:
    if(pattern.match(item)):
        print(item,'은 조건에 적합')
        totallist.append(item)    # totallist에 적합한 항목 추가
    else :
        print(item, '은 조건에 부적합')

print(totallist)