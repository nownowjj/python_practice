# alice png 파일 검은 배경에 steve.txt wordcloud를 입히는 py
from PIL import Image  # PIL Python Image Library

image_file = 'alice.png'  # 파일명
img_file = Image.open(image_file) # img_file에 저장
print(type(img_file))
print('-'*30)

import numpy as np
alice_mask = np.array(img_file)
print(alice_mask)
print('-'*30)

import matplotlib.pyplot as plt
plt.figure(figsize= (8,8))
plt.imshow(alice_mask,interpolation='bilinear')
plt.axis('off') # 축 제거
filename = 'graph01.png'
plt.savefig(filename)
print(filename + '파일 저장')

from wordcloud import WordCloud,STOPWORDS

# 불용어(STOPWORD) : 빈도 수는 많지만, 분석에 절대적이지 않은 단어들
mystopwords = set(STOPWORDS) # 집합
mystopwords.add('said')
mystopwords.update(['hohoho','hahaha'])
# print(mystopwords)
# print('-'*30)
                # 배경색 하얗게  업근된 단어중에서 빈도가 제일높은거 2000개    불용어 적용  alice그림에다 그려줘
wc = WordCloud(background_color='white',max_words=2000 ,stopwords=mystopwords,mask=alice_mask)

stevefile = 'steve.txt'         # steve 텍스트 파일
text =open(stevefile,'rt',encoding='UTF-8')
text = text.read()

wc = wc.generate(text)

plt.figure(figsize=(12,12))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
filename = 'graph02.png'
plt.savefig(filename)
print(filename +'파일 저장')


#--------------------------
alice_color_file='alice_color.png'
alice_color_mask =  np.array(Image.open(alice_color_file))

wc = WordCloud(background_color='white',max_words=2000,stopwords=mystopwords,\
               mask=alice_color_mask,max_font_size=40,random_state=42)

wc = wc.generate(text)

plt.figure(figsize=(12,12))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
filename = 'graph03.png'
plt.savefig(filename)
print(filename +'파일 저장')


#------------------------------------------
plt.figure(figsize=(12,12))
plt.imshow(alice_color_mask,interpolation='bilinear')
plt.axis('off')
filename = 'graph04.png'
plt.savefig(filename)
print(filename +'파일 저장')

#----------------------
wc = WordCloud(background_color='white',max_words=2000 ,stopwords=mystopwords,mask=alice_mask)

heartfile = 'heart-of-darkness.txt'         # steve 텍스트 파일
text =open(heartfile,'rt',encoding='UTF-8')
text = text.read()

wc = wc.generate(text)
plt.figure(figsize=(12,12))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
filename = 'graph05.png'
plt.savefig(filename)
print(filename +'파일 저장')
#-------------------------------

from wordcloud import ImageColorGenerator

image_colors = ImageColorGenerator(alice_color_mask)
newwc = wc.recolor(color_func=image_colors)

plt.figure(figsize=(12,12))
plt.imshow(newwc,interpolation='bilinear')
plt.axis('off')
filename = 'graph06.png'
plt.savefig(filename)
print(filename + '파일 저장')