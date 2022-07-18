coffee = 3
price = 2000

print('판매 가능한 커피 잔량 : %d' % (coffee))
print('단가 : %d ' % (price))

while True :
    money = int(input('돈을 넣어 주세요 : '))
    if money == price :
        print('커피를 판매합니다.')
        coffee -=1
    elif money > price :
        print('거스름돈 {}를 주고 , 1잔을 팝니다.'.format(money-price))
        coffee -=1
    else :
        print('금액이 부족하여 판매 불가능합니다.')

        print('남은 커피의 양은 {}잔입니다.'.format(coffee))


    if coffee == 0 :
        print('커피 다 팔렸어요')
        break
