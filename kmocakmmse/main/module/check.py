import numpy as np
import pandas as pd

def check_answer(ch):
    CHECKANSWER = {'1': '예', '0': '아니오', '-': '모름', 'M': '남자', 'F': '여자', 'R': '오른손', 'L': '왼손', 'B': '양손',
                0: '무학문맹', 0.5: '무학문해', None: '미입력', '': '미입력'}
    
    if ch in CHECKANSWER:
        return CHECKANSWER[ch]
    else:
        return ch

def char2int(ch):
    if ch == 'M':
        return 1
    elif ch == 'F':
        return 0