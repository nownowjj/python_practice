import json,urllib.request ,math
import folium

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('UTF-8')
    except Exception as err:
        return None
#end def getRequestUrl

def getCultureData(pageNo,nPage):
    end_point = 'http://apis.data.go.kr/6290000/eventbaseinfo/geteventbaseinfo'

    access_key = 'C1dyxQ8J4rsqoxWObuS8zyvOOxuJB2iBmxSs9Q58iZed0ubWowzekp%2B%2FxQa194cEvlhLqqNCziGOyYHYEw9N9g%3D%3D'

    parameters = ''
    parameters += '?resultType=json' + ''
    parameters += '&serviceKey=' + access_key
    parameters += '&pageNo=' + str(pageNo)
    parameters += '&numOfRows=' + str(numOFRows)

    url = end_point + parameters
    print(url)
    result = getRequestUrl(url)
    if result == None:
        return None
    else:
        return result
#end def getCultureData

pageNo = 1
numOFRows =1
nPage = 0

import xml.etree.ElementTree as ET

dataList = []
lat = []
lng = []

while(True):
    print('pageNo : %d, nPage : %d ' %(pageNo,nPage))
    xmldata = getCultureData(pageNo,numOFRows)
    # print(xmldata)
    xmlTree = ET.fromstring(xmldata)

    if (xmlTree.find('header').find('resultMsg').text == 'Normal Service'):
        totalCount = int(xmlTree.find('header').find('totalCount').text) # 데이터 총 개수
        # print('총개수 : %d' % totalCount) # 135개

        if totalCount == 0:
            break

        listTree = xmlTree.find('body').findall('item') # body안에 item들

        for node in listTree: # item별로 반복문 실행
           eventNm = node.find('eventNm').text   # 행사명
           eventVenue = node.find('eventVenue').text # 장소
           eventInfo = node.find('eventInfo').text #행사내용
           eventBeginDate = node.find('eventBeginDate').text #행사 시작일자
           eventEndDate = node.find('eventEndDate').text #행사 종료일자
           eventBeginTime = node.find('eventBeginTime').text # 행사 시작시각
           eventEndTime = node.find('eventEndTime').text #행사 종료시각
           lat =node.find('lat').text # 위치 좌표 위도
           lng =node.find('lng').text # 위치 좌표 경도
           onedict = {'행사명':eventNm,'장소':eventVenue,\
                      '행사내용':eventInfo,'행사 시작일자':eventBeginDate,\
                      '행사 종료일자':eventEndDate,'행사 시작시각':eventBeginTime,\
                      '행사 종료시각':eventEndTime,'위도':lat,'경도':lng}
           dataList.append(onedict)

        nPage = math.ceil(totalCount/numOFRows)  # 135 / 100  = 1

        # marker = folium.Marker([lat, lng], popup=eventNm, icon=folium.Icon(icon='info-sign')).add_to(map_osm)
        #
        # mylatitude = 37.56
        # mylongitude = 126.92
        # map_osm = folium.Map(location=[mylatitude, mylongitude], zoom_start=13)


        if pageNo == nPage:
            break
        pageNo += 1
    else:
        break
#end while


# filename = 'map_result333.html'
# map_osm.save(filename)
# print(filename + '파일 저장 완료')
# print('finished')

import pandas as pd
savedFilename = 'deajon.csv'
myframe = pd.DataFrame(dataList)
myframe.to_csv(savedFilename)
print(savedFilename,'파일 저장완료')







