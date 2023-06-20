from gensim.models import Word2Vec

# 모델 로딩
model = Word2Vec.load('nvmc.model')
print('사랑 : ', model.wv['사랑'])

# 단어 유사도 계산
print("일요일 = 월요일\t", model.wv.similarity(w1='일요일', w2='월요일'))
print("일요일 = 배우\t", model.wv.similarity(w1='안성기', w2='배우'))
print("일요일 = 대기업\t", model.wv.similarity(w1='대기업', w2='삼성'))
print("일요일 = 삼성\t", model.wv.similarity(w1='일요일', w2='삼성'))
print("일요일 = 삼성\t", model.wv.similarity(w1='히어로', w2='삼성'))