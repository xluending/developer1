from konlpy.tag import Komoran

#komoran = Komoran(userdic='./user_dic.tsv')
komoran = Komoran(userdic='./Chatbot/data/user2.dic')
#text = "우리 챗봇은 엔엘피를 좋아해."x
text = "우리 챗봇은 엔와이피를 뉴진스를 좋아해."
pos = komoran.pos(text)
print(pos)