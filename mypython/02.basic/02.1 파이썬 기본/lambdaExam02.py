x = int(input('정수1 :'))
y = int(input('정수2 :'))
examlambda = lambda x,y : x**3 - (y+2)

result = examlambda(x,y)
print(result)
