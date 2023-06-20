from konlpy.tag import Kkma

# 꼬꼬마 형태소 분석기 객체 생성
kkma = Kkma()
text = "공극의 질문 중 '당신이 귀하다고 추구하며 살아온 것은 무엇인가요?' 에 내 대답은 '꿈, 정' 이었다. 책 <죽음의 수용소에서> 에서도 자살한 사람과 그렇지 않은 사람의 차이는 목표와 꿈이었다. 여태 힘든 시간을 보냈어도 나를 완성하는 과정이고 성장 중이라는 걸 안다. 그리고 온전한 나를 그리는 건 내 꿈이다. 공극에 참여할 수 있었던 건 좋은 행운이었다."

mprphs = kkma.morphs(text)
sentence = kkma.sentences(text)

print(mprphs)
print(sentence)