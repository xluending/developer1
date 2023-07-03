import sys
sys.path.append(r"C:\Users\user\Desktop\developer\Chatbot")
from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='C:/Users/user/Desktop/developer/Chatbot/train_tools/dict/chatbot_dict.bin',
               userdic='C:/Users/user/Desktop/developer/Chatbot/utils/user_dic.tsv')

intent = IntentModel(model_name='../models/intent/intent_model.h5', proprocess=p)
query = "오늘 탕수육 주문 가능한가요?"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)

