#예제-5-1  2-gram 유사도 계산
from konlpy.tag import Komoran
# 어절 단위 n-gram 1
def word_ngram(bow, num_gram):
    text = tuple(bow)
    ngrams = [text[x:x + num_gram] for x in range(0, len(text))]
    return tuple(ngrams)
 
# 유사도 계산 2
def similarity(doc1, doc2):
    cnt = 0
    for token in doc1:
        if token in doc2:
            cnt = cnt + 1
    return cnt/len(doc1)
 
print("3개 이상의 단어로 구성된 문장1을(를) 입력하세요")
print("예 : 사람은 포유류에 속하는 동물이다")
sentence1 = input("문장1 : ")
print("3개 이상의 단어로 구성된 문장2을(를) 입력하세요")
print("예 : 사람은 설치류에 속하는 동물이다")
sentence2 = input("문장2 : ")
 
# 형태소 분석기에서 명사(단어) 추출 3
komoran = Komoran()
bow1 = komoran.nouns(sentence1)
bow2 = komoran.nouns(sentence2)
 
# 단어 n-gram 토큰 추출 4
doc1 = word_ngram(bow1, 2) # 2-gram 방식으로 추출
doc2 = word_ngram(bow2, 2) # 3 -> 3묶음씩 하나의 토큰
 
# 추출된 n-gram 토큰 출력
print(doc1)
print(doc2)


# 유사도 계산  
r1 = similarity(doc1, doc2) # 5


# 계산된 유사도 출력
print(r1)