from bs4 import BeautifulSoup

filename = 'css01.html'
myencoding = 'UTF-8'
myparser = 'html.parser'

html = open(filename,encoding='UTF-8')
soup = BeautifulSoup(html,myparser)
print(type(soup))

# div id가 cartoon인 영역에 h1의 문자열
h1 = soup.select_one('div#cartoon > h1').string
print('h1=',h1)

li_list = soup.select('div#cartoon > ul.elements > li')
for li in li_list:
    print('li=',li.string)

print('-'*30)
choice = lambda x : print(soup.select_one(x).string)

choice('#item5')

choice('li#item4')

choice('ul > li#item3')

choice('#itemlist #item2')

choice('#itemlist > #item3')

choice('ul#itemlist > li#item2')

choice("li[id='item1']")

print('-'*5,'zzzz')
choice("#itemlist li:nth-of-type(1)")
choice("#itemlist li:nth-of-type(2)")
choice("#itemlist li:nth-of-type(3)")
choice("#itemlist li:nth-of-type(4)")
choice("#itemlist li:nth-of-type(5)")
print('-'*5)
choice("li:nth-of-type(1)")
choice("li:nth-of-type(2)")
choice("li:nth-of-type(3)")
choice("li:nth-of-type(4)")
choice("li:nth-of-type(5)")
print('-'*5,'zzzz')

print('+'*30)
print(soup.select('li')[1].string)
print('+'*30)

print(soup.select('li')[4].string)
print('+'*30)

mytag = soup.select_one('div#cartoon > ul.elements')
print(mytag)
print('+'*30)
                            # 1베이스
mystring =mytag.select_one('li:nth-of-type(3)').string
print(mystring)
print('+'*30)

mytag = soup.select_one('ul#itemlist') # 1베이스
mystring = mytag.select_one('li:nth-of-type(4)').string
print(mystring)
print('+'*30)

print(soup.select('#vegatables > li[class="us"]')[0].string)
print('+'*30)

print(soup.select('#vegatables > li.us')[1].string)
print('+'*30)

result = soup.select('a[href$=".com"]')
for item in result :
    print(item['href'])
print('+' * 30)

result = soup.select('a[href*="daum"]')
for item in result:
    print(item['href'])

print('+'*30)

cond = {'id':'ko','class':'cn'} #id가 ko이고 class가 cn
print(soup.find('li',cond).string)
print('+'*30)
            # li의 cond의 string

print(soup.find(id='vegatables').find('li',cond).string)
print('+'*30)

import re

li = soup.find_all(href=re.compile('^https://'))
for item in li:
    print(item.attrs['href'])