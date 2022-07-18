import re
from ChickenUtil import ChickenStore
##    모듈                클래스 이름
############################################
brandName ='nene'
base_url='https://nenechicken.com/17_new/sub_shop01.asp'
############################################
def getData():
    saveData = []
    for page_idx in range(1,45+1):
        url = base_url + '?page=%d' %(page_idx)
        chknStore = ChickenStore(brandName,url)
        soup = chknStore.getSoup()

        tablelist = soup.findAll('table',attrs={'class':'shopTable'})
        # print(len(tablelist))

        print(page_idx)
        for onetable in tablelist:
            store = onetable.select_one('.shopName').string
            # print(store)
            temp = onetable.select_one('.shopAdd').string
            # print(temp)

            im_address = onetable.select_one('.shopMap')
            im_address = im_address.a['href']
            # print(im_address)  #ex : JAVASCRIPT:codeAddress('경기도포천시왕방로159');

            if temp == None : # shopAdd 항목이 없는 매장
                apos = im_address.find("(")
                dpos = im_address.find(")")
                temp = im_address[apos+1:dpos].replace("'","")
                address = temp
                sido = ''  #how to ??
                gungu = '' #how to ??
            else:
                regex = '\d\S*'  # 숫자로 시작하고 최소한 0번이상 , 패턴 생성
                pattern = re.compile(regex)  # 패턴 컴파일
                mymatch = pattern.search(im_address)  # 패턴으로 잘라냄
                # print(mymatch)  # 잘라낸거 확인

                addr_suffix = mymatch.group().replace("');", "")  # ' ) ; 공백으로
                address = temp + '' + addr_suffix
                # print(address)

                imsi = temp.split(' ')
                sido = imsi[0]
                gungu = imsi[1]
            # end if
            # print(store +'/' + temp)

            # if temp == '':
            # else:
            #     pass

            phone = onetable.select_one('.tooltiptext').string

            mydata = [brandName,store,sido,gungu,address,phone]
            saveData.append(mydata)

            # print('-'*30)
        # if page_idx == 3:
        #     break

    chknStore.save2Csv(saveData)

############################################
print(brandName + '매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')