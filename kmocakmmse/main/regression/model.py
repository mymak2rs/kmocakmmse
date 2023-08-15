import statsmodels.api as sm
import joblib
import sys
import numpy as np

sys.path.append('./')

kmoca_sum_target = ['K-MoCA_시공간/집행기능_1-가->5-마', 'K-MoCA_시공간/집행기능_육면체 그리기',
       'K-MoCA_시공간/집행기능_시계 그리기 (윤곽)', 'K-MoCA_시공간/집행기능_시계 그리기 (숫자)',
       'K-MoCA_시공간/집행기능_시계 그리기 (바늘)', 'K-MoCA_이름대기_사자', 'K-MoCA_이름대기_박쥐',
       'K-MoCA_이름대기_낙타', 'K-MoCA_주의력_순서대로 따라 외우기', 'K-MoCA_주의력_거꾸로 따라 외우기',
       'K-MoCA_주의력_요일 손뼉치기', 'K-MoCA_주의력_100-7-7-7-7-7',
       'K-MoCA_언어_칼날같이 날카로운 바위', 'K-MoCA_언어_스물 일곱 개의 찬 맥주병이 냉장고에 있다',
       'K-MoCA_언어_"ㄱ"으로 시작되는 단어 (6개 단어 이상)', 'K-MoCA_추상력_기차-비행기',
       'K-MoCA_추상력_시계-저울', 'K-MoCA_지연회상_얼굴', 'K-MoCA_지연회상_비단',
       'K-MoCA_지연회상_학교', 'K-MoCA_지연회상_피리', 'K-MoCA_지연회상_노랑', 'K-MoCA_지남력_일',
       'K-MoCA_지남력_월', 'K-MoCA_지남력_년', 'K-MoCA_지남력_요일', 'K-MoCA_지남력_장소',
       'K-MoCA_지남력_도시 이름']



def mocab_pentagon_LR(input):
    model = joblib.load('D:/DBLab/kmocakmmse/kmocakmmse/kmocakmmse/main/regression/datasetB/best_model_b_pentagon.pkl')
    predict = np.round(model.predict_proba(input)*100, 2)
    return predict.ravel()

def mocab_LR(input):
    model = joblib.load('D:/DBLab/kmocakmmse/kmocakmmse/kmocakmmse/main/regression/datasetB/best_model_b.pkl')
    predict = np.round(model.predict_proba(input)*100, 2)
    return predict.ravel()

def mocad_pentagon_LR(input):
    model = joblib.load('D:/DBLab/kmocakmmse/kmocakmmse/kmocakmmse/main/regression/datasetD/best_model_d_pentagon.pkl')
    predict = np.round(model.predict_proba(input)*100, 2)
    return predict.ravel()

def mocad_LR(input):
    model = joblib.load('D:/DBLab/kmocakmmse/kmocakmmse/kmocakmmse/main/regression/datasetD/best_model_d.pkl')
    predict = model.predict_proba(input).round(4)*100
    return predict.ravel()