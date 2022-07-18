import json,urllib.request ,math


def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('UTF-8')
    except Exception as err:
        return None

def getHospitalData(pageNo,numOFRows):
    # 앤드 포인트
    end_point = 'http://apis.data.go.kr/6260000/MedicInstitService/MedicalInstitInfo'

    # 일반 인증키
    access_key = 'C1dyxQ8J4rsqoxWObuS8zyvOOxuJB2iBmxSs9Q58iZed0ubWowzekp%2B%2FxQa194cEvlhLqqNCziGOyYHYEw9N9g%3D%3D'

    parameters = ''
    parameters += '?resultType=json' + ''
    parameters += '&serviceKey=' + access_key
    parameters += '&pageNo=' + str(pageNo)
    parameters += '&numOfRows=' + str(numOFRows)

    url = end_point + parameters

    # print('유알엘')
    # print(url)

    result = getRequestUrl(url)
    if result == None :
        return None
    else :
        return json.loads(result)

pageNo = 1
numOFRows =100
nPage = 0

jsonResult = [] # 결과를 담을 곳

while(True):
    print('pageNo : %d ,nPage : %d' % (pageNo,nPage))
    jsondata = getHospitalData(pageNo,numOFRows)
    # print(jsondata)

    if(jsondata['MedicalInstitInfo']['header']['code'] =='00'):
        totalCount = jsondata['MedicalInstitInfo']['totalCount']
        # print('데이터 총 개수 : %d' % totalCount) #전체 6846개

        if totalCount == 0 :
            break

        # print(len(jsondata['MedicalInstitInfo']['item'])) #100개

        for item in jsondata['MedicalInstitInfo']['item']:
            jsonResult.append(item)  # item을 jsonResult에 담음

        nPage = math.ceil(totalCount / numOFRows)
        if(pageNo == nPage) : #  끝 페이지 이면
            break

        pageNo += 1

    else :
        break

#end while

savedFilename = '부산시 의료 기관, 약국 운영시간 정보.json'
with open(savedFilename,'wt',encoding='UTF-8')as outfile:
    retJson = json.dumps(jsonResult,indent=4, sort_keys=True , ensure_ascii=False)
    outfile.write(retJson)

print(savedFilename + '파일 저장')