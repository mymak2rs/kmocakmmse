import pandas as pd
import numpy as np

def find_closest(A, target):
    #A must be sorted
    idx = A.searchsorted(target)
    idx = np.clip(idx, 1, len(A)-1)
    left = A[idx-1]
    right = A[idx]
    idx -= target - left < right - target
    return idx

def MoCA_cutoff(age, edu, moca_score):
    """MoCA cutoff 점수 계산 함수

    Parameters:
    - age: 나이
    - edu: 교육 기간

    Returns:
    - MoCA cutoff 점수
    """
    bmoca_data = pd.read_csv('D:/DBlab/kmocakmmse/kmocakmmse/main/module/criterion/MoCA_NC_VS_MCI+PDD_중간나이 교육 별 분포 LR 추가_20230825.csv', encoding='cp949')
    dmoca_data = pd.read_csv('D:/DBlab/kmocakmmse/kmocakmmse/main/module/criterion/MoCA_NC+MCI_VS_PDD_중간나이 교육 별 분포 LR 추가_20230825.csv', encoding='cp949')

    # A열, B열, C열의 모든 나이 값 추출
    all_ages = list(bmoca_data["중심 나이"].values) + list(bmoca_data[">=-5"].dropna().values) + list(bmoca_data["<+5"].dropna().values)
    min_age = min(all_ages)
    max_age = max(all_ages)

    # 입력된 나이가 모든 나이보다 작거나 크면, 각각의 최저나이와 최고나이를 기준으로 설정
    if age < min_age:
        age = min_age
    elif age > max_age:
        age = max_age

    # "중심 나이"에서 입력 나이에 가장 근접한 값을 찾기 위해 함수 호출
    moca_x = find_closest(bmoca_data["중심 나이"].values, age)
    closest_age = bmoca_data.iloc[moca_x]["중심 나이"]

    # 교육 수준에 따른 열 이름 결정
    if edu == 0:
        moca_y = "0년(비문해)"
    elif 0.5 <= edu <= 3:
        moca_y = "0.5 ~ 3년"
    elif 4 <= edu <= 6:
        moca_y = "4 ~ 6년"
    elif 7 <= edu <= 9:
        moca_y = "7 ~ 9년"
    elif 10 <= edu <= 12:
        moca_y = "10 ~ 12년"
    else:
        moca_y = "13년 이상"

    # 나이가 특정 범위에 속하는 경우 B열, C열의 특정 행 값을 사용
    if 50 <= age <= 55 or 80 <= age <= 85 or 85 <= age <= 94:
        if age in bmoca_data[">=-5"].values:
            moca_x = bmoca_data[bmoca_data[">=-5"] == age].index[0]
        elif age in bmoca_data["<+5"].values:
            moca_x = bmoca_data[bmoca_data["<+5"] == age].index[0]

    # 데이터 프레임에서 해당하는 나이와 교육 수준에 따른 MoCA cutoff 점수 가져오기
    b_cutoff_score = bmoca_data.iloc[moca_x][moca_y]
    d_cutoff_score = dmoca_data.iloc[moca_x][moca_y]

    # MoCA cutoff 점수 반환
    return b_cutoff_score, d_cutoff_score

# def MMSE_cutoff(age, edu, mmse_score):
#     if edu == 0:
#         mmse_y = 0
#     elif 0.5 <= edu <= 3:
#         mmse_y = 1
#     elif 4 <= edu <= 6:
#         mmse_y = 2
#     else:
#         mmse_y = 3
        
#     if age < 65:
#         mmse_x = 0
#     elif 65 <= age <= 69:
#         mmse_x = 1
#     elif 70 <= age <= 74:
#         mmse_x = 2
#     elif 75 <= age <= 84:
#         mmse_x = 3
#     else:
#         mmse_x = 4     
    
    
#     # mmse_arr = np.array([[19.95, 24.7, 26.03, 26.89, 27.51, 27.99, 28.4],
#     #                     [19.71, 24.53, 25.91, 26.79, 27.43, 27.93, 28.35],
#     #                     [19.33,	24.25, 25.68, 26.62, 27.3, 27.83, 28.26],
#     #                     [18.78, 23.83, 25.39, 26.38, 27.11, 27.68, 28.15],
#     #                     [18.05, 23.3, 24.98, 26.07, 26.86, 27.49, 28],
#     #                     [17.17, 22.65, 24.49, 25.69, 26.56, 27.24, 27.81],
#     #                     [16.11, 21.86, 23.89, 25.21, 26.18, 26.95, 27.57],
#     #                     [14.85, 20.92, 23.18, 24.66, 25.75, 26.6, 27.3],
#     #                     [13.4, 19.84, 22.36, 24.01, 25.23, 26.19, 26.97]]
#     #                    )
    
#     # 0 MMSE 규준.jpg
#     mmse_arr = np.array([[18.47, 23.01, 25.08, 25.02],
#                          [16.80, 22.15, 23.40, 24.40],
#                          [15.59, 21.83, 22.59, 24.14],
#                          [14.56, 20.41, 21.12, 22.65],
#                          [11.72, 18.49, 19.83, 26.38]])
    
#     mmse_m_arr = np.array([[21.33, 25.85, 27.20, 27.77],
#                            [20.13, 25.40, 26.18, 27.20],
#                            [19.33, 25.19, 26.05, 27.09],
#                            [18.05, 24.26, 25.23, 26.41],
#                            [15.73, 22.67, 24.00, 28.50]])
    
#     mmse_sd_arr = np.array([[2.86, 2.84, 2.12, 2.75],
#                             [3.33, 3.25, 2.78, 2.80],
#                             [3.74, 3.36, 3.46, 2.95],
#                             [3.49, 3.85, 4.11, 3.76],
#                             [4.01, 4.18, 4.17, 2.12]])
    
#     cutoff_score = mmse_arr[mmse_x, mmse_y]
#     m = mmse_m_arr[mmse_x, mmse_y]
#     sd = mmse_sd_arr[mmse_x, mmse_y]
    
#     mmse_zscore = '-'
    
#     if mmse_score != None:
#         mmse_zscore = np.round(((mmse_score-m)/sd), 2)
    
#     return cutoff_score, mmse_zscore

# def MMSE2_cutoff(age, edu):
#     mmse2_x = (age-40)//5 + 1 if age >= 40 else 0
    
#     if age == 90:
#         mmse2_x = 10
#     elif age > 90:
#         mmse2_x = 10
    
#     if edu == 0:
#         mmse2_y = 0
#     elif 0.5 <= edu <= 5:
#         mmse2_y = 1
#     elif 6 <= edu <= 8:
#         mmse2_y = 2
#     elif 9 <= edu <= 11:
#         mmse2_y = 3
#     elif 12 <= edu <= 15:
#         mmse2_y = 4
#     else:
#         mmse2_y = 5
         
#     mmse2_arr = np.array([[22.51, 26.09, 26.19, 26.89, 28.16, 28.7],
#                           [21.44, 25.13, 25.26, 25.96, 27.33, 27.91],
#                           [21.25, 24.99, 25.15, 25.86, 27.23, 27.83],
#                           [20.96, 24.79, 24.99, 25.7, 27.11, 27.72],
#                           [20.52, 24.5, 24.8, 25.5, 26.94, 27.56],
#                           [19.88, 24.09, 24.53, 25.25, 26.71, 27.34],
#                           [19.01, 23.54, 24.2, 24.92, 26.4, 27.04],
#                           [17.84, 22.81, 23.76, 24.49, 26.01, 26.66],
#                           [16.35, 21.88, 23.24, 23.96, 25.5, 26.17],
#                           [14.12, 20.71, 22.58, 23.31, 24.88, 25.57],
#                           [12.14, 19.29, 21.79, 22.52, 24.13, 24.84]]
#                        )
    
#     return mmse2_arr[mmse2_x, mmse2_y]



# def MoCA_cutoff(age, edu, moca_score):
#     midle_age = np.array([57, 62, 67, 72, 77, 82])

#     moca_x = find_closest(midle_age, age)
    
#     if edu == 0:
#         moca_y = 0
#     elif 0.5 <= edu <= 3:
#         moca_y = 1
#     elif 4 <= edu <= 6:
#         moca_y = 2
#     elif 7 <= edu <= 12:
#         moca_y = 3
#     else:
#         moca_y = 4
    
#     # 0 MoCA 규준.jpg
#     moca_arr = np.array([[10, 15, 19, 22, 27],
#                          [10, 15, 17, 21, 24],
#                          [9, 14, 16, 20, 24],
#                          [8, 14, 16, 19, 23],
#                          [8, 13, 16, 19, 23],
#                          [7, 13, 15, 17, 21]]
#                        )
    
#     moca_m_arr = np.array([[13.43, 19.67, 21.66, 24.11, 27.00],
#                            [13.43, 18.53, 20.30, 22.75, 25.75],
#                            [12.12, 17.02, 19.77, 22.64, 25.32],
#                            [11.29, 16.69, 19.11, 22.25, 24.87],
#                            [10.43, 16.30, 19.29, 22.12, 24.58],
#                            [9.33, 16.50, 18.54, 20.57, 23.56]])
    
#     moca_sd_arr = np.array([[4.20, 5.32, 2.96, 2.48, 1.00],
#                            [4.20, 4.10, 4.03, 2.72, 2.22],
#                            [3.90, 3.61, 3.88, 2.94, 1.46],
#                            [3.72, 3.58, 4.11, 3.31, 2.05],
#                            [3.30, 3.48, 3.78, 3.51, 2.26],
#                            [2.69, 3.58, 4.01, 3.96, 3.17]])
    
#     cutoff_score = moca_arr[moca_x, moca_y]
#     m = moca_m_arr[moca_x, moca_y]
#     sd = moca_sd_arr[moca_x, moca_y]
#     moca_zscore = '-'
    
#     if moca_score != None:
#         moca_zscore = np.round(((moca_score-m)/sd), 2)
    
#     return cutoff_score, moca_zscore