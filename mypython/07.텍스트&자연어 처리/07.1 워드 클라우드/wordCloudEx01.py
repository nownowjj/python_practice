import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
filename = 'steve.txt'
myfile = open(filename,'rt',encoding='utf-8')
text = myfile.read()
print(type(text))
print('-'*30)

from wordcloud import WordCloud

wordcloud = WordCloud()
wordcloud = wordcloud.generate(text)
print(type(wordcloud))
print('-'*30)

bindo = wordcloud.words_
print(type(bindo))
print('-'*30)

# print(bindo)
# print('-'*30)

# 사전이므로 정렬이 필요합니다.
sortedData = sorted(bindo.items(),key=lambda x:x[1],reverse=True)
print(type(sortedData))
print('-'*30)

chartdata = sortedData[0:10]

xtick =[] # x 축에 놓이는 문자열
chart =[] # x 그래프 그릴 데이터
for item in chartdata:
    xtick.append(item[0])
    chart.append(item[1])

import matplotlib.pyplot as plt

plt.bar(xtick,chart)
plt.title('상위 빈도 top 10')
filename = 'wordCloudEx01_01.png'
plt.savefig(filename)
print(filename + '파일 저장')

plt.figure(figsize=(12,12))
plt.imshow(wordcloud) # image show
plt.axis('off') # 축 없애기
filename = 'wordCloudEx01_02.png'
plt.savefig(filename)
print(filename + '파일 저장')

