import numpy as np
import pandas as pd

def check_answer(ch):
    CHECKANSWER = {'1': '예', '0': '아니오', '-': '모름', 'M': '남자', 'F': '여자', 'R': '오른손', 'L': '왼손', 'B': '양손',
                0: '무학문맹', 0.5: '무학문해', None: '미입력'}
    
    if ch in CHECKANSWER:
        return CHECKANSWER[ch]
    else:
        return ch

def char2int(ch):
    if ch == 'M':
        return 1
    elif ch == 'F':
        return 0

def handle_file(file):
    df = pd.read_excel(file, engine='openpyxl',sheet_name=0)

    # 유효성 검사를 해야하는 col 범위 지정, 데이터가 아예 없는 col은 제거

    df = df.iloc[:, 3:]
    df = df.dropna(how='all', axis=1)
    df.columns = [i for i in range(1, len(df.columns) + 1)]
    df_mc = df.iloc[20:85,]
    df_null_sum = df_mc.isnull().sum().to_list()
    for i in df_null_sum:
      if(i==65):
        return False, "MMSE, MoCA 중 하나의 검사라도 입력해 주세요."
    
    # Na 값들 None으로 변경
    df = df.where(pd.notnull(df), None)

    # 필수항목 값 유무 체크
    df_essential = df.iloc[[0, 1, 2, 3, 4, 5, 19]]
    
    # 필수가 아닌 행들 6~18, 60~61, 69, 77~78
    drop_row = [6, 7, 8, 9, 10, 11, 12, 13,
                14, 15, 16, 17, 18, 60, 61, 69, 77, 78]

    df_clear = df.drop(index=drop_row, axis=0)

    # 결측값 갯수로 판단
    null_sum = df_essential.isnull().sum().to_list()

    if df_essential.empty:
        return False, '값이 들어있지 않습니다.'
    
    for i in null_sum:
        if(i!=0):
            return False, '필수입력 항목을 확인해주세요.'


    # 필수 입력 값이 전부 들어있는 파일 입력 양식 검사
    # 3, 4, 68 행은 문자열을 숫자로 변경하여 숫자인지 확인

    hospital = ['YSV', 'HLS', 'SEV', 'KHG', 'GSV']
    sex = ['M', 'F']
    hand = ['R', 'L', 'B']
    snsb = ['NC', 'SCD', 'MCI', 'Dmt']
    zero_one = [0, 1,None]
    zero_three = [0, 1, 2, 3,None]

    df_n = df_clear.loc[[3, 4]]
    try:
        df_n = df_n.astype(float)
    except:    # 3, 4행 중 숫자가 아닌 것이 포함되어 있을 시, 에러메세지 수정 필요
        return False, '숫자만 입력해주세요.'

    final = df_clear.loc[[0], :].isin(hospital)
    final = pd.concat([final,df_clear.loc[[2],:].isin(sex)])
    final = pd.concat([final, df_clear.loc[[5], :].isin(hand)])
    final = pd.concat([final, df_clear.loc[[19], :].isin(snsb)])
    

    for i in range(20, 60):
        final = pd.concat([final, df_clear.loc[[i], :].isin(zero_one)])
    for i in range(62, 65):
        final = pd.concat([final, df_clear.loc[[i], :].isin(zero_one)])

    final = pd.concat([final, df_clear.loc[[65], :].isin(zero_three)])
    final = pd.concat([final, df_clear.loc[[66], :].isin(zero_one)])
    final = pd.concat([final, df_clear.loc[[67], :].isin(zero_one)])

    for i in range(70, 77):
        final = pd.concat([final, df_clear.loc[[i], :].isin(zero_one)])
    for i in range(79, 85):
        final = pd.concat([final, df_clear.loc[[i], :].isin(zero_one)])

    # 올바른 값이면 1, 아니면 0으로 매핑
    final = final.astype(int)

    # 열의 합이 63이 나오면 전부 올바른 값
    colcnt = 0
    for i in range(1, len(final.columns)+1):
        if (final[i].sum() != 63):   # 에러메세지 수정 필요
            return False, "잘못된 입력방식입니다. 엑셀파일을 확인해주세요."
        else:
            colcnt += 1
    
    df_clear= df.loc[[3,4,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 68]]
    
    age = list(df_clear.loc[3])
    education = list(df_clear.loc[4])
    parkinson_disease = list(df_clear.loc[9])
    diag_duration = list(df_clear.loc[10])
    hy = list(df_clear.loc[12])
    mupdrs = list(df_clear.loc[13])
    sgds = list(df_clear.loc[14])
    k_mmse = list(df_clear.loc[15])
    k_mmse2 = list(df_clear.loc[16])
    k_moca = list(df_clear.loc[17])
    moca_k = list(df_clear.loc[18])
    mc_fluency = list(df_clear.loc[68])
    
    def none_exist(my_list):
        li = [i for i in my_list if i is not None]
        if not li:
            return '1'
        return li

    if ''.join(map(str, none_exist(diag_duration))).replace('.', '').isdigit() != True:
        return False, '파킨슨 병의 유병기간은 숫자만 입력해주세요.'
    
    if ''.join(map(str, none_exist(mc_fluency))).isdigit() != True:
        return False, '단어 갯수는 숫자만 입력해주세요.'
    
    if ''.join(map(str, none_exist(hy))).replace('.', '').isdigit() != True:
        return False, 'H&Y stage는 숫자만 입력해주세요.'
    
    if ''.join(map(str, none_exist(mupdrs))).isdigit() != True:
        return False, 'Motor UPDRS 점수는 숫자만 입력해주세요.'
    
    if ''.join(map(str, none_exist(sgds))).isdigit() != True:
        return False, 'SGDS 점수는 숫자만 입력해주세요.'
    
    if ''.join(map(str, none_exist(k_mmse))).isdigit() != True:
        return False, 'K-MMSE 점수는 숫자만 입력해주세요.'
    
    if ''.join(map(str, none_exist(k_mmse2))).isdigit() != True:
        return False, 'K-MMSE~2 점수는 숫자만 입력해주세요.'
    
    if ''.join(map(str, none_exist(k_moca))).isdigit() != True:
        return False, 'K-MoCA 점수는 숫자만 입력해주세요.'
    
    if ''.join(map(str, none_exist(moca_k))).isdigit() != True:
        return False, 'MoCA-K 점수는 숫자만 입력해주세요.'

    num = 0
    for i,j,k in zip(parkinson_disease, diag_duration, age):
        if ((i == 0) or (i == None)) and (j != None):
            if j == 0:
                pass
            else:
                return False, f"{num+1}번 환자의 파킨슨병 진단여부를 확인해주세요."
        if (i == 1) and (j == None):
            return False, f"{num+1}번 환자의 유병기간을 입력해주세요."
        if (j != None ) and (k < j):
            return False, f'{num+1}번 환자의 나이가 유병기간보다 적습니다.'
        if (j != None ) and (j < 0):
            return False, f'{num+1}번 환자의 유병기간을 정확히 입력해주세요.'
        num += 1


    for i in [age-education for age,education in zip(age,education)]:
        if(i < 0):
            return False, "나이가 학력보다 적습니다."

    for i in age:
        if i<0 or i > 120:
            return False, "나이를 정확히 입력해주세요."

    for i in education:
        if i<0:
            return False, "학력을 정확히 입력해주세요."

    for i in hy:
        if(i != None) and ((i<1) or (i>5)):
            return False, "H&Y 척도를 정확히 입력해주세요.(1 이상 5 이하)"
    
    for i in mupdrs:
        if (i != None) and (i < 0):
            return False, "Motor UPDRS 점수를 확인해주세요."

    for i in sgds:
        if(i<0)or(i>15):
            return False, "H&Y 척도를 정확히 입력해주세요.(0 이상 15 이하)"

    for i in k_mmse:
        if (i != None) and ((i<0)or(i>30)):
            return False, "KMMSE 점수를 확인해주세요. (0 이상 30이하)"

    for i in k_mmse2:
        if (i != None) and ((i<0)or(i>30)):
            return False, "KMMSE2 점수를 확인해주세요. (0 이상 30이하)"

    for i in k_moca:
        if (i != None) and ((i < 0)or(i > 30)):
            return False, "K_MoCA 점수를 확인해주세요. (0 이상 30이하)"

    for i in moca_k:
        if (i != None) and ((i<0)or(i>30)):
            return False, "MoCA_K 점수를 확인해주세요. (0 이상 30이하)"

    
    df_clear= df.loc[[3,4,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
    
    df_clear.loc[[6, 7, 8, 9, 11]] = df_clear.loc[[6, 7, 8, 9, 11]].fillna('-')
    df.loc[[6, 7, 8, 9, 11]] = df.loc[[6, 7, 8, 9, 11]].fillna('-')
    
    zero_one_na = [0, 1, '-']
    
    if False in np.concatenate((df_clear.loc[[6, 7, 8, 9, 11]].isin(zero_one_na)).to_numpy().tolist()):
        return False, "잘못된 입력방식입니다. 엑셀 파일을 확인해주세요."   # 에러메세지 수정 필요
        
        
    # 단어 개수 확인
    moca_mocak = list(df.loc[51])
    mc_fluency = list(df.loc[68])
    mc_fluency_n = list(df.loc[69])
    
    num = 1
    for i, j, k in zip(moca_mocak, mc_fluency, mc_fluency_n):
        if (k == None) and (i == 0):
            df[num][69] = 1 if j >= 6 else 0
        elif (k == None) and (i == 1):
            df[num][69]  = 1 if j >= 11 else 0

        if (i == 0) and ((j >= 6 and k == 0) or (j < 6 and k == 1)):
            return False, '{0}번 환자의 K-MoCA 단어 개수에 따른 점수가 맞지 않습니다.'.format(num)
        if (i == 1) and ((j >= 11 and k == 0) or (j < 11 and k == 1)):
            return False, '{0}번 환자의 MoCA-K 단어 개수에 따른 점수가 맞지 않습니다.'.format(num)
        num += 1
        
        
    # MMSE, MoCA 총점 비교
    moca_drop_row = [60,61,68,77,78]
    
    i = 1
    for kmmse, kmmse2, kmoca, mocak in zip(k_mmse, k_mmse2, k_moca, moca_k):
        mmse = list(df[i][20:51])
        moca = list((df[i][51:85]).drop(index=moca_drop_row, axis=0))
        
        if (kmmse != None) and (mmse[0] == 0):
            if (0 in mmse or 1 in mmse) and (None in mmse):
                return False, '{0}번 환자에 입력되지않은 K-MMSE 항목이 있습니다.'.format(i)
            elif sum(mmse[1:]) != kmmse:
                return False, '{0}번 환자의 K-MMSE 총점이 다릅니다.'.format(i)
                
        if (kmmse2 != None) and (mmse[0] == 1):
            if (0 in mmse or 1 in mmse) and None in mmse:
                return False, '{0}번 환자에 입력되지않은 K-MMSE~2 항목이 있습니다.'.format(i)
            elif sum(mmse[1:]) != kmmse2:
                return False, '{0}번 환자의 K-MMSE~2 총점이 다릅니다.'.format(i)
                
        if (kmoca != None) and (moca[0] == 0):
            if (0 in moca or 1 in moca) and None in moca:
                return False, '{0}번 환자에 입력되지않은 K-MoCA 항목이 있습니다.'.format(i)
            elif sum(moca[1:]) != kmoca:
                return False, '{0}번 환자의 K-MoCA 총점이 다릅니다.'.format(i)
                
        if (mocak != None) and (moca[0] == 1):
            if (0 in moca or 1 in moca) and None in moca:
                return False, '{0}번 환자에 입력되지않은 MoCA-K 항목이 있습니다.'.format(i)
            elif sum(moca[1:]) != mocak:
                return False, '{0}번 환자의 MoCA-K 총점이 다릅니다.'.format(i)
        i += 1
    
    
    return True, [len(df), len(df.columns), df]