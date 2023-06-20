from konlpy.tag import Komoran

#komoran = Komoran(userdic='./user_dic.tsv')
komoran = Komoran(userdic='./Chatbot/data/tt.dic')
#text = "우리 챗봇은 엔엘피를 좋아해."
text = "들국화와 산울림 중 최고의 그룹은 누구일까"
text1 = "들국화는 국화꽃과 다를까?"
pos = komoran.pos(text)
pos1 = komoran.pos(text1)
print(pos)
print(pos1)