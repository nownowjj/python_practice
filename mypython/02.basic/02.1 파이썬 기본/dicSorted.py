wordInfo = {'세탁기':50,'선풍기':30,'청소기':40,'냉장고':60}

myxticks = sorted(wordInfo,key=wordInfo.get,reverse=True) # 내림차순
print(myxticks)

reverse_key = sorted(wordInfo.keys(),reverse=True)
print(reverse_key)

chardata = sorted(wordInfo.values(),reverse=True)
print(chardata)