import folium, requests

baseurl = 'https://dapi.kakao.com/v2/local/search/address.json?query='

api_key='78e612bf0e2496232729ea58e519fcf3'
header = {'Authorization' : 'KakaoAK ' + api_key}
# print(header)

def makeMap(brand , store, geoinfo):
    shopname = store + '(' + brand + ')'
    mycolor = brand_color[brand]
    latitude, longitude = float(geoinfo[0]), float(geoinfo[1])
    marker = folium.Marker([latitude,longitude],popup=shopname,\
                icon=folium.Icon(color=mycolor,icon='info-sign')).add_to(map_osm)

# 지도의 기준점
mylatitude = 37.56
mylongitude = 126.92
map_osm = folium.Map(location=[mylatitude, mylongitude], zoom_start=13)

brand_dict = {'cheogajip':'처가쥡','nene':'눼눼치킨'} # 브랜드 한글이름
brand_color = {'cheogajip':'red','nene':'blue'} # 브랜드 색

def getGeocoder(address):
    result = ''
    url = baseurl + address
    r = requests.get(url, headers=header)
    # print(type(r))

    if r.status_code == 200:
        try:
            result_address = r.json()["documents"][0]['address']
            # print(result_address)
            result = result_address['y'],result_address['x']
            return result
        except Exception as err:
            return None
    else:
        result = 'error[' + str(r.status_code) + ']'
        return result

import pandas as pd

csv_file = 'allStoreModified.csv'
myframe = pd.read_csv(csv_file,index_col=0,encoding='utf-8')
# print(myframe)

where = '서대문구'
brandname = 'cheogajip'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandname
mapData01 = myframe.loc[condition1 & condition2]
# print(mapData01)
# print(len(mapData01))
# print('-'*30)


brandname = 'nene'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandname
mapData02 = myframe.loc[condition1 & condition2]
# print(mapData02)
# print(len(mapData02))

mylist = []
mylist.append(mapData01)
mylist.append(mapData02)

mapData = pd.concat(mylist,axis=0)
# print(mapData)
# print('-'*30)

ok = 0 # 주소 변환이 잘 된 개수
notok = 0
for idx in range(len(mapData.index)):
    brand = mapData.iloc[idx]['brand']
    store = mapData.iloc[idx]['store']
    address = mapData.iloc[idx]['address']
    geoinfo = getGeocoder(address)

    if geoinfo == None:
        print('낫오케이 :' +address)
        notok += 1
    else :
        print('오케이 :' + brand + ' ' + address)
        ok += 1
        makeMap(brand , store ,geoinfo)
    print('-'*30)

print('ok : ' + str(ok))
print('notok : ' + str(notok))

filename = 'map_result.html'
map_osm.save(filename)
print(filename + '파일 저장 완료')
print('finished')