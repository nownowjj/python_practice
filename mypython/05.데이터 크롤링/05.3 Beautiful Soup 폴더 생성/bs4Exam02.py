from bs4 import BeautifulSoup
html = open('fruits.html','r',encoding='UTF-8')
soup = BeautifulSoup(html,'html.parser')
body = soup.select_one('body')
print(type(body))
print(body)

ptag = body.find('p') # find 1개 찾기
# print(type(ptag))
# print(ptag)

print(ptag['class']) # 속성읽기

ptag['id'] = 'apple' # 신규 속성 만들기
print(ptag['id'])

body_tag = soup.find('body')

idx = 0
for child in body_tag.children:
    idx += 1
    # print(str(idx) + '번째 요소')
    # print(child)

print('-'*30)
mydiv = soup.find('div')
print(mydiv)

print('-'*30)
print('div의 부모는?')
print(mydiv.parent)

print('-'*30)
mytag = soup.find('p',attrs={'class':'hard'})
print(mytag)

print('-'*30)
print('mytag의 부모는?')
print(mytag.find_parent())

parents = mytag.find_parent()
for p in parents:
    print(p.name)