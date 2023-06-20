from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()
# text = "자극과 반응 사이에는 공간이 존재한다."
# text = "내가 지금까지 이렇게 애를 쓴 건 내가 바라는 멋진 내 모습이 있기 때문이다."
text = "책 <죽음의 수용소에서>에서도 자살한 사람과 그렇지 않은 사람의 차이는 목표와 꿈이었다. "

nouns = komoran.nouns(text)
print(nouns)

# 단어 사전 구축 및 단어별 인덱스 부여
dics = {}
for word in nouns :
    if word not in dics.keys():
        dics[word] = len(dics)
print(dics)

# 원-핫 인코딩
nb_classes = len(dics)
targets = list(dics.values())
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)