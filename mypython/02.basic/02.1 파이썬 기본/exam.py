#2개의 정수를 입력받아 덧셈 수행 프로그램
# no1 = int(input('첫번째 수 :'))
# no2 = int(input('두번째 수 :'))
#
# result = no1 + no2
# print(result)
#
# #품목 이름과 수량과 단가를 입력받아 총 금액을 구하는 프로그램
# prname = input('품목 이름 : ')
# prqty = int(input('수량 입력'))
# prprice = int(input('단가 입력 : '))
# prtotal = prqty * prprice

# print('품목 : %s , 수량 :%d , 단가 : %d , 총 금액 :  %d'%(prname,prqty,prprice,prtotal))

#정수 1개를 입력받아서 짝수이면 제곱 , 홀수이면 3제곱 프로그램
# no = int(input('정수 입력'))
# if(no % 2 == 0) :
#     print(no ** 2)
# else :
#     print(no ** 3)

# +연산자를 사용하면 2개의 리스트를 합침. 리스트를 합치고 %3 =1 요소만 출력
# lista = ['김의찬','유만식','이영철']
# listb = ['심수련','윤기석','노윤희']
# listab = (lista+listb)
# length = len(listab)
# print(listab[1:length:3])

#
fruits = [('바나나',10),('수박',20),('오렌지',15)]

mydict = dict()

for key, value in fruits :
    mydict[key] = value  # mydict이라는 빈 사전에 fruits key ,value로 사전구성
print(mydict) # 사전에 담김

# 사전[a] = b # put
# 사전[a] # get
