salary = int(input('급여 입력 : ')) # 급여
income = 0
tax = 0

print('년소득 구하기') # 자바 if문과는 다르게 : 가 들어감
if salary >= 500 :
    income = 12 * salary
else :
    income = 13 * salary

print('세금 구하기')
if income >= 10000 :
    tax = 0.2 * income
elif income >= 7000 :
    tax = 0.15 * income
elif income >= 5000 :
    tax = 0.12 * income
elif income >= 1000 :
    tax = 0.1 * income
else :
    tax = 0

print('급여 :%d' % (salary))
print('연소득 :%.2f' % (income))
print('세금 :%.2f' % (tax))