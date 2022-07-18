import folium, requests

baseurl = 'https://dapi.kakao.com/v2/local/search/address.json?query='

api_key='78e612bf0e2496232729ea58e519fcf3'
header = {'Authorization' : 'KakaoAK ' + api_key}
# print(header)

def makeMap(brand , store, geoinfo):
    shopname = store + '(' + brand + ')'  # ex ~~점 (nene)
    mycolor = brand_color[brand]    # ex nene면 blue
    latitude, longitude = float(geoinfo[0]), float(geoinfo[1])  #위도 경도  : 33~~~ ,23~~
                                        # 마커에 위치  , popup= ex~~점(nene)
    marker = folium.Marker([latitude,longitude],popup=shopname,\
                icon=folium.Icon(color=mycolor,icon='info-sign')).add_to(map_osm)

# 지도의 기준점
mylatitude = 33.40
mylongitude = 126.55
map_osm = folium.Map(location=[mylatitude, mylongitude], zoom_start=13)

brand_dict = {'cheogajip':'처가집','nene':'네네치킨','palicana':'페리카나','goobne':'굽네'} # 브랜드 한글이름
brand_color = {'cheogajip':'red','nene':'blue','palicana':'black','goobne':'yellow'} # 브랜드 색

def getGoocoder(address):
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

where = '제주특별자치도'
brandname = 'cheogajip'
condition1 = myframe['sido'] == where
condition2 = myframe['brand'] == brandname
mapData01 = myframe.loc[condition1 & condition2]
# print(mapData01)
# print(len(mapData01))
# print('-'*30)


brandname = 'nene'
condition1 = myframe['sido'] == where
condition2 = myframe['brand'] == brandname
mapData02 = myframe.loc[condition1 & condition2]
# print(mapData02)
# print(len(mapData02))

brandname = 'goobne'
condition1 = myframe['sido'] == where
condition2 = myframe['brand'] == brandname
mapData03 = myframe.loc[condition1 & condition2]
# print(mapData03)
# print(len(mapData03))

brandname = 'palicana'
condition1 = myframe['sido'] == where
condition2 = myframe['brand'] == brandname
mapData04 = myframe.loc[condition1 & condition2]
# print(mapData04)
# print(len(mapData04))

mylist = []
mylist.append(mapData01)  # 각 매장별 data 1,2,3,4
mylist.append(mapData02)
mylist.append(mapData03)
mylist.append(mapData04)

mapData = pd.concat(mylist,axis=0) # 각 매장별 리스트 concat
# print(mapData)
# print('-'*30)

ok = 0 # 주소 변환이 잘 된 개수
notok = 0
for idx in range(len(mapData.index)):   # 전체 매장수 만큼 반복문 실행
    brand = mapData.iloc[idx]['brand']  #  매장명
    store = mapData.iloc[idx]['store']  #  가게명
    address = mapData.iloc[idx]['address'] # 주소
    geoinfo = getGoocoder(address) #위도,경도

    if geoinfo == None:
        print('낫오케이 :' +address)
        notok += 1
    else :
        print('오케이 :' + brand + ' ' + address)
        ok += 1
        makeMap(brand , store ,geoinfo)   # 브랜드명 , 가게명 ,위,경도
    print('-'*30)

print('ok : ' + str(ok))
print('notok : ' + str(notok))

filename = 'map_result2.html'
map_osm.save(filename)
print(filename + '파일 저장 완료')
print('finished')