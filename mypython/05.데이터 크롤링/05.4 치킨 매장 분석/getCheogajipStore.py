from itertools import count
from ChickenUtil import ChickenStore
############################################
brandName ='cheogajip'
base_url='http://www.cheogajip.co.kr/bbs/board.php'
############################################
def getData():
    saveData = []
    for page_idx in count():
        url = base_url + '?bo_table=store'
        url += '&page=%s' %str(page_idx+1)

        chknStore = ChickenStore(brandName,url)
        soup = chknStore.getSoup()
        # print(type(soup))
        print(page_idx+1)

        mytbody = soup.find('tbody')
        shopExists = False # False이면 매장 목록이 없음

        for mytr in mytbody.findAll('tr'):
            shopExists =True

            try:
                store = mytr.select_one('td:nth-of-type(2)').string
                address = mytr.select_one('td:nth-of-type(3)').string #서울특별시 중랑구 용마산로109길 24
                phone = mytr.select_one('td:nth-of-type(4)').string
                imsi = address.split(' ')
                sido = imsi[0]   #ex : 서울특별시
                gungu = imsi[1]  #ex : 중랑구

                saveData.append([brandName,store,sido,gungu,address,phone])
            except AttributeError as err:  #매장이 더이상 존재하지 않음
                print('마지막 페이지에 도달하였습니다.')
                shopExists = False
                break
        # print('-'*30)

        if shopExists == False:
            chknStore.save2Csv(saveData)
            break

        # if page_idx >= 2:  # 3번만 돌려보기 테스트 느낌
        #     chknStore.save2Csv(saveData)
        #     break
############################################
print(brandName + '매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')