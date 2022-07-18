import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

class ChickenStore():
    def getWebDriver(self,cmdJavaScript):
        self.driver.execute_script(cmdJavaScript)
        wait = 1
        time.sleep(wait)
        mypage = self.driver.page_source

        return BeautifulSoup(mypage,'html.parser')

    # 해당 리스트를 사용하여 csv 파일을 생성해 줍니다.
    def save2Csv(self,saveData):
        data = pd.DataFrame(saveData,columns=self.mycolumns)
        data.to_csv(self.brandName +'.csv',\
                    encoding=self.myencoding,\
                    index=True)

    def __init__(self,brandName,url):
        self.brandName = brandName
        self.url = url
        self.myencoding = 'UTF-8'
        self.soup = self.get_request_url()

        # csv 파일에 들어갈 컬럼 헤더
        self.mycolumns =['brand','store','sido','gungu','address','phone']

        if self.brandName != 'goobne':  # 굽네가 아닌 매장
            self.soup = self.get_request_url()
            self.driver = None  # driver 객체 필요가 없음

        else:  # 굽네 매장 전용
            self.soup = None
            filepath = 'D:/chromedriver_win32/chromedriver.exe'
            self.driver = webdriver.Chrome(filepath)
            self.driver.get(self.url)

        # print('생성자 호출됨')


    # BeautifulSoup 객체를 반환해 주는 함수
    def getSoup(self): #BeautifulSoup 객체를 반환해 주는 함수
        if self.soup == None:
            return None
        else:
            return BeautifulSoup(self.soup, 'html.parser')

    # urlopen 함수를 이용하여 url 객체를 반환해주는 함수
    def get_request_url(self):
        request = urllib.request.Request(self.url)
        try:
            response = urllib.request.urlopen(request)
            if response.getcode() == 200 : #http 응답 코드가 정상
                if self.brandName !='pelicana':
                    return response.read().decode(self.myencoding)
                else:
                    return response
        except Exception as err :
            print(err)
            return None



# end claas ChickenStore