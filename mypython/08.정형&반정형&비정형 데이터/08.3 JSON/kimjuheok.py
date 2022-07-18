import json

filename = '김주혁_naver_news.json'
myfile = open(filename,'rt',encoding='utf-8')
myfile = myfile.read()
# print(data)

jsondata = json.loads(myfile)
# print(jsondata)

for item in jsondata :
    print('타이틀 : ' , item['title'])
    print('설명 : ' , item['description'])
    print('\n')


