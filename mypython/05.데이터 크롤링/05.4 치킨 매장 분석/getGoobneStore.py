from itertools import count
from ChickenUtil import ChickenStore
############################################
brandName ='goobne'
base_url='http://www.goobne.co.kr/store/search_store.jsp'
############################################
def getData():
    saveData = []
    chknStore = ChickenStore(brandName,base_url)  # 다른 치킨 사이트는 클릭한 번호를 넘김

    for page_idx in count():
        print('%s 페이지가 호출되었습니다.' %str(page_idx+1))
        bEndPage = False # True이면 마지막 페이지가 됩니다.

        # 1,2,3,4,5,6~~~~~ 클릭시 커맨드를 넘겨줌
        cmdJavaScript = "javascript:store.getList('%s')" %str(page_idx+1)
        soup =chknStore.getWebDriver(cmdJavaScript)
        # print(type(soup))

                    # 매장 리스트가 id가 store_list -- tbody에 있음
        store_list = soup.find('tbody',attrs={'id':'store_list'})
        mytrlists = store_list.findAll('tr')

        for onestore in mytrlists :
            mytdlists = onestore.findAll('td')

            if len(mytdlists) > 1 :  # tr에 td가 존재하면 데이터 받아옴
                store = onestore.select_one('td:nth-of-type(1)').get_text(strip=True) #매장명
                phone = onestore.select_one('td:nth-of-type(2)').a.string  # 번호 데이터
                address = onestore.select_one('td:nth-of-type(3)').a.string # 주소 데이터
                imsi = str(address).split(' ') #주소를 공백으로 split시킴
                sido = imsi[0]  # ex : 경기도
                gungu = imsi[1] # ex : 화성시

                saveData.append([brandName,store,sido,gungu,address,phone])
            else :  # tr에 td가 없다는 뜻은 더이상 매장정보가 없다는 뜻임
                bEndPage = True  # 마지막임
                break
        print('-'*30)

        # if page_idx >= 1 :  # 테스트용 2번만 실행
        #     break

        if bEndPage == True :
            break

    chknStore.save2Csv(saveData)
############################################
print(brandName + '매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')