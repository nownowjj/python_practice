somelist = ['김의찬','유만식','이영철','심수련','윤기석','노윤회','황우철']
print(somelist)

print(somelist[4])

print(somelist[-2])

print(somelist[1:4])  # 1,2,3

print(somelist[4:]) # 4부터 끝까지

length = len(somelist)
print(length)

# print(somelist[:]) # 모두 다

# 슬라이싱[시작 : 종점 : 증감치]
print(somelist[1:length:2])
print(somelist[0:length:2])
