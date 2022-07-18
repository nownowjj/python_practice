from konlpy.tag import Komoran

sentense = '코로나 바이러스 태블릿 PC, 김지원 , 가나다라'
print('사전 사용전')
komo = Komoran()
print(komo.pos(sentense))
print('-'*30)

print('사전 사용후')
komo = Komoran(userdic='user_dic.txt')
print(komo.pos(sentense))
print('-'*30)

print('komo.nouns')
print(komo.nouns(sentense))
print('-'*30)

print('komo.mprphs')
print(komo.morphs(sentense))
print('-'*30)