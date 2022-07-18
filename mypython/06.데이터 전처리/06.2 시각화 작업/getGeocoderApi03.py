import folium, requests

address = '경기도 광명시 광명로 942번길 20-2'

url = 'https://dapi.kakao.com/v2/local/search/address.json?query='  + address

api_key='78e612bf0e2496232729ea58e519fcf3'
header = {'Authorization' : 'KakaoAK ' + api_key}
# print(header)

def getGoocoder(address):
    result = ''
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

address_latlng = getGoocoder(address)
latitude = address_latlng[0]
longitude = address_latlng[1]

print('주소 : ' +address + '위도: ' + latitude + '경도: ' + longitude)

shopname = '경기도 광명점'
map_osm = folium.Map(location=[latitude, longitude], zoom_start=17)
folium.Marker([latitude, longitude], popup=shopname, icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)
folium.CircleMarker([latitude, longitude], radius = 150, color='blue', fill_color='red', popup=shopname).add_to(map_osm)
map_osm.save('my_map_graph.html')

print('작업 종료')