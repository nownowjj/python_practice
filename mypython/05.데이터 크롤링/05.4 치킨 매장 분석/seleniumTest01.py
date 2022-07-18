from selenium import webdriver
from selenium.webdriver.common.by import By

filename = 'D:/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(filename)
print(type(driver)) # webDriver 객체
print('-'*20)

print('구글로 이동합니다')
url="http://www.google.com"  # url 경로 설정
driver.get(url)         # url로 이동

# search_textbox = driver.find_element_by_name('q')
search_textbox = driver.find_element(by=By.NAME,value='q')

word='북미정상회담'
search_textbox.send_keys(word)

search_textbox.submit()

import time

wait = 3
print(str(wait) + '초 대기')
time.sleep(wait)

imagefile ='capture.png'
driver.save_screenshot(imagefile)
print(imagefile + ' 파일로 저장')

wait = 3
print(str(wait) + '초후 종료')
driver.implicitly_wait(wait)

driver.quit()










# # 웹페이지가 로딩되기까지 시간이 필요해서 sleep을 이용해서 조금 기다립니다.
# time.sleep(0.5) ## 0.5초
#
# # driver.find_element_by_name(<element의 name>).send_keys(<검색어>)
# element = driver.find_element_by_name('q')
# element.send_keys("북미정상회담")
# element.submit()