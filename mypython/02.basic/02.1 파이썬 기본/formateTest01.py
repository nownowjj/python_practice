coffee = 3
price = 2000

print('우리 매장에는 커피가{}잔이 있습니다.'.format(coffee))

money = int(input('돈을 넣어 주세요 : ')) # 3000
print('{}원을 입금하셨습니다.'.format(money))

change = money - price
print('거스름돈은 {}원이며 , 커피 {}잔을 판매합니다.'.format(change,1))
print('남은 커피의 잔은 {}잔입니다.'.format(coffee-1))