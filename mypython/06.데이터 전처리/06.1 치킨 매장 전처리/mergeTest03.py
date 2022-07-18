import pandas as pd

print('mystore')
mystorefile = 'store.csv'
mystore = pd.read_csv(mystorefile,encoding='UTF-8',index_col=0,header=0)
print(mystore)
print('-'*30)

print('district')
districtfile = 'districtmini.csv'
district = pd.read_csv(districtfile,encoding='UTF-8',header=0)
print(district)
print('-'*30)

print('result')
result = pd.merge(mystore,district,on=['sido','gungu'],how='outer',suffixes=['','_'],indicator=True)
print(result)
print('-'*30)

print('m_result')
m_result = result.query('_merge == "left_only"')
print(m_result)
print('-'*30)

print('gungu_list')
gungufile = open('gungufile.txt',encoding='utf-8')
gungu_list = gungufile.readlines()
print(gungu_list)
print('-'*30)


print('gungu_dict')
gungu_dict = {}
for onegu in gungu_list:
    mydata = onegu.replace('\n','').split(':') # 스플릿하면 리스트
    gungu_dict[mydata[0]] = mydata[1]

print(gungu_dict)
print('-'*30)


# mystore에 있는 gungu컬럼에 apply하겠다
mystore.gungu = mystore.gungu.apply(lambda data : gungu_dict.get(data,data))

print('최종 결과')
print(mystore)
print('-'*30)