dictionary = {'김유신':50,'윤봉길':0,'김구':60}

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

for key, value in dictionary.items():
    print({'{}의 나이는 {}살입니다.'.format(key,value)})

for key in dictionary.keys() :
    print('{}의 나이는 {}살입니다.'.format(key,dictionary[key]))

findkey = '유관순'
if findkey in dictionary :  # 유관순이 dictionary에 있냐
    print(findkey + '는 존재함')
else :
    print(findkey +' 는 존재안함')

result = dictionary.pop('김구')
print(dictionary)
print(result)

dictionary.clear()
print(dictionary)