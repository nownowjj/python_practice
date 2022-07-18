from itertools import count
from ChickenUtil import ChickenStore
##    모듈                클래스 이름
############################################
brandName ='palicana'
base_url='https://www.pelicana.co.kr/store/stroe_search.html'
############################################
def getData():
    saveData = [] # 엑셀로 저장될 중첩 리스트 구조
    for page_idx in count():
        url = base_url + '?page=' + str(page_idx+1)
        # print(url)

        chknStore = ChickenStore(brandName,url) # 생성자 호출
        soup = chknStore.getSoup()
        # print(type(soup))

        mytable = soup.find('table',attrs={'class':'table mt20'})
        mytbody = mytable.find('tbody')
        # print(len(mytbody.find_all('tr')))

        shopExists = False # 매장 목록이 없다고 가정
        for mytr in mytbody.findAll('tr'):
            shopExists = True  # 매장 목록이 존재하면 출력
            mylist = list(mytr.strings)
            # print(mylist)
            # print('#'*30)
            #  ex : ['\n', '가경동점', '\n', '충청북도 청주시흥덕구 풍산로 103(복대동)', '\n', '\r\n\t\t\t\t\t\t\t\t043-233-4091', '\n', '상세정보','\n']

            store = mylist[1]   #ex 가경동점
            address = mylist[3] # ex 충청북도 청주시흥덕구 풍산로 103(복대동)
            # print('{' + address + '}')

            imsiphone = mytr.select_one('td:nth-of-type(3)').string
            if imsiphone != None:
                phone = imsiphone.strip()  # 공백 제거
            else:
                phone = ""

            if(len(address)) >= 2 :
                imsi = address.split() #{충청북도 청주시흥덕구 풍산로 103(복대동)}
                sido = imsi[0] # 충청북도
                gungu = imsi[1] # 청주시흥덕구

                mydata = [brandName,store,sido,gungu,address,phone]
                # print(mydata)
                saveData.append(mydata)


        # print('-'*30)
        if shopExists == False:# 매장 목록이 없으면 출력 멈춤
            chknStore.save2Csv(saveData)
            break

        # if page_idx >= 2:
        #     chknStore.save2Csv(saveData)
        #     break
############################################
print(brandName + '매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')