from django import forms
import main.module.choice as choice

class PatientForm(forms.Form):
    patient_no = forms.CharField(
        label='환자번호',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'patient_num',
                'placeholder': '환자번호',
                'id': 'patient_num'
            }
        ),
        error_messages={
            'required': '환자번호를 입력해주세요.',
            'unique': '중복된 환자 번호입니다.',
            'max_length': '환자번호가 너무 깁니다. (45자 이내로 적어주세요.)'
            }
    )
    
    sex = forms.CharField(
        label='성별',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SEX,
            attrs={
                'class': 'sex',
                'id': 'sex',
            }
        ),
        error_messages={'required': '성별을 선택해주세요.'}
    )
    age = forms.IntegerField(
        label='나이',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'age',
                'placeholder': '00 세',
                'id': 'age'
            }
        ),
        error_messages={'required': '나이를 입력해주세요.'}
    )

    education = forms.FloatField(
        label='교육 연한(년)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_EDU,
            attrs={
                'class': 'edu',
                'id': 'edu'
            }
        ),
        error_messages={'required': '교육 연한을 입력해주세요.'}
    )

    edu_input = forms.FloatField(
        label='',
        required=False,
        widget=forms.NumberInput(
            attrs={'placeholder': '00년'}
        )
    )

    kmoca_total = forms.IntegerField(
        label='K-MoCA 점수',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'kmoca_total',
                'placeholder': 'K-MoCA 점수 입력',
                'id': 'kmoca_total'
            }
        )
    )
    handedness = forms.CharField(
        label='주 사용 손',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_HAND,
            attrs={
                'class': 'hand',
                'id': 'hand'
            }
        ),
        error_messages={'required': '주 사용 손을 선택해주세요.'}
    )
    patient_cog_compl = forms.CharField(
        label='환자가 기억력 저하를 느낍니까?',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_YES_NO,
            attrs={
                'class': 'pat_cog',
                'id': 'pat_cog'
            }
        ),
        error_messages={'required': '환자 기억력 저하 여부를 선택해주세요.'}
    )
    caregiver_cog_compl = forms.CharField(
        label='보호자가 환자의 기억력 저하를 느낍니까?',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_YES_NO,
            attrs={
                'class': 'care_cog',
                'id': 'care_cog'
            }
        ),
        error_messages={'required': '보호자의 환자 기억력 저하 여부를 선택해주세요.'}
    )
    neurologic_problems = forms.CharField(
        label='뇌경색, 뇌출혈 진단을 받은 적이 있습니까?',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_ANSWER,
            attrs={
                'class': 'neu_prob',
                'id': 'neu_prob'
            }
        ),
        error_messages={'required': '뇌경색, 뇌출혈 진단의 여부를 선택해주세요.'}
    )
    parkinson_disease = forms.CharField(
        label='파킨슨병 진단을 받은 적이 있습니까?',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_ANSWER,
            attrs={
                'class': 'parkins',
                'id': 'parkins'
            }
        ),
        error_messages={'required': '파킨슨병의 여부를 선택해주세요.'}
    )
    diag_duration = forms.FloatField(
        label='파킨슨병의 유병 기간(months)',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'dia_duration',
                'placeholder': '00 개월',
                'id': 'dia_duration'
            }
        )
    )
    depression = forms.CharField(
        label='우울증으로 진단받은 적이 있습니까?',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_ANSWER,
            attrs={
                'class': 'depress',
                'id': 'depress'
            }
        ),
        error_messages={'required': '우울증 여부를 선택해주세요.'}
    )
    sgds_bdi_depression = forms.CharField(
        label='SGDS 혹은 BDI로 우울증을 진단받은 적이 있습니까?',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_YES_NO,
            attrs={
                'class': 'sgds_bdi_depression',
                'id': 'sgds_bdi_depression'
            }
        ),
        error_messages={'required': 'SGDS 혹은 BDI 우울증 여부를 선택해주세요.'}
    )
    hy_stage = forms.FloatField(
         label='H&Y 척도',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'hy',
                'placeholder': 'H&Y 척도 입력',
                'id': 'hy'
            }
        )
    )
    motor_updrs_score = forms.IntegerField(
        label='Motor UPDRS (UPDRS Part III) 점수',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'updrs',
                'placeholder': 'Motor UPDRS 점수 입력',
                'id': 'updrs'
            }
        )
    )
    sgds_score = forms.IntegerField(
        label='Short Version of Geriatric Depression Scale (SGDS) 점수',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'sgds',
                'placeholder': 'SGDS 점수 입력',
                'id': 'sgds'
            }
        )
    )

    class Meta:
        fields = [
            'patient_no',
            'sex',
            'age',
            'education',
            'edu_input',
            'handedness',
            'patient_cog_compl',
            'caregiver_cog_compl',
            'neurologic_problems',
            'parkinson_disease',
            'diag_duration',
            'depression',
            'sgds_bdi_depression',
            'hy_stage',
            'motor_updrs_score',
            'sgds_score',
            'kmoca_total',
        ]


    def clean(self):
        cleaned_data = super().clean()
        patient_no = cleaned_data.get('patient_no', '')
        sex = cleaned_data.get('sex', '')
        age = cleaned_data.get('age', '')
        education = cleaned_data.get('education', '')
        edu_input = cleaned_data.get('edu_input', '')
        kmoca_total = cleaned_data.get('kmoca_total', '')
        handedness = cleaned_data.get('handedness', '')
        patient_cog_compl = cleaned_data.get('patient_cog_compl', '')
        caregiver_cog_compl = cleaned_data.get('caregiver_cog_compl', '')
        neurologic_problems = cleaned_data.get('neurologic_problems', '')
        parkinson_disease = cleaned_data.get('parkinson_disease', '')
        diag_duration = cleaned_data.get('diag_duration', '')
        sgds_bdi_depression = cleaned_data.get('sgds_bdi_depression', '')
        depression = cleaned_data.get('depression', '')
        hy_stage = cleaned_data.get('hy_stage','')
        motor_updrs_score = cleaned_data.get('motor_updrs_score','')
        sgds_score = cleaned_data.get('sgds_score','')

        if (education == 999) and (edu_input == None):
            return self.add_error('edu_input', '교육연한을 입력해주세요.')
        
        if ((parkinson_disease == '0') or (parkinson_disease == '-')) and (diag_duration != None):
            if diag_duration == 0:
                pass
            else:
                return self.add_error('parkinson_disease', '파킨슨병 진단 여부를 확인해주세요.')
        
        if (parkinson_disease == '1') and (diag_duration == None):
            return self.add_error('diag_duration', '유병기간을 입력해주세요.')
    
        if (parkinson_disease == '1') and (age < diag_duration/12):
            return self.add_error('age', '나이가 유병기간보다 적습니다.')
    
        if (parkinson_disease == '1') and (diag_duration <= 0):
            return self.add_error('diag_duration', '유병기간을 정확히 입력해주세요.')

        if (age < education) and (education != 999):
            return self.add_error('age', '나이가 학력보다 적습니다.')
        
        if (edu_input != None) and (age < edu_input):
            return self.add_error('age', '나이가 학력보다 적습니다.')
        
        if age > 120:
            return self.add_error('age', '나이를 정확히 입력해주세요.')
    
        if age < 0:
            return self.add_error('age', '나이를 정확히 입력해주세요.')

        if education < 0:
            return self.add_error('education', '학력을 정확히 입력해주세요.')
    
        if (hy_stage != None) and (hy_stage < 1 or hy_stage > 5):
            return self.add_error('hy_stage', 'H&Y 척도를 정확히 입력해주세요.(1 이상 5 이하)')
    
        if (motor_updrs_score != None) and (motor_updrs_score < 0):
            return self.add_error('motor_updrs_score', 'Motor UPDRS 점수를 확인해주세요.')

        if (sgds_score != None) and (sgds_score < 0 or sgds_score > 15):
            return self.add_error('sgds_score', 'SGDS 점수를 확인해주세요. (0 이상 15이하)')

        if (not (kmoca_total == None)) and (kmoca_total > 30) | (kmoca_total < 0):
            return self.add_error('kmoca_total', 'K-MoCA 점수를 확인해주세요. (0 이상 30이하)')
    
        
        self.patient_no = patient_no
        self.sex = sex
        self.age = age
        self.education = education        
        self.edu_input = edu_input
        self.handedness = handedness
        self.patient_cog_compl = patient_cog_compl
        self.caregiver_cog_compl = caregiver_cog_compl
        self.neurologic_problems = neurologic_problems
        self.parkinson_disease = parkinson_disease
        self.diag_duration = diag_duration
        self.depression = depression
        self.sgds_bdi_depression = sgds_bdi_depression
        self.hy_stage = hy_stage
        self.motor_updrs_score = motor_updrs_score
        self.sgds_score = sgds_score
        self.kmoca_total = kmoca_total
        
        
class KMoCAForm(forms.Form):
    mc_atm = forms.CharField(
        label='1-가-2-나-3-다',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA1',
                'name': 'KMoCA1'
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_cube = forms.CharField(
        label='육면체 그리기',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA2',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_clock_cont = forms.CharField(
        label='시계 그리기 (윤곽)',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA3',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_clock_num = forms.CharField(
        label='시계 그리기 (숫자)',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA4',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_clock_hands = forms.CharField(
        label='시계 그리기 (바늘)',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA5',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_lion = forms.CharField(
        label='사자',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA6',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_bat = forms.CharField(
        label='박쥐',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA7',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_camel = forms.CharField(
        label='낙타',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA8',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )

    mc_re_1 = forms.IntegerField(
        label='1차 점수',
        required=False,
        widget=forms.NumberInput(
            attrs = {
                'class' : 'KMoCA',
                'placeholder':'1차 점수 입력',
                'id' : 'KMoCA9'
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )    
    
    mc_re_2 = forms.IntegerField(
        label='2차 점수',
        required=False,
        widget=forms.NumberInput(
            attrs = {
                'class' : 'KMoCA',
                'placeholder':'2차 점수 입력',
                'id' : 'KMoCA10'
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    ) 

    mc_forward = forms.CharField(
        label='순서대로 따라 외우기',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA11',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_backward = forms.CharField(
        label='거꾸로 따라 외우기',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA12',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_vigilance = forms.CharField(
        label='요일 손벽치기',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA13',
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_serial_7s = forms.CharField(
        label='100-7-7-7-7-7',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_MOCA12_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA14',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_sentence_1 = forms.CharField(
        label='칼날같이 날카로운 바위',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA15',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_sentence_2 = forms.CharField(
        label='스물 일곱 ... 냉장고에 있다',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA16',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_fluency = forms.CharField(
        label='"ㄱ"으로 시작되는 단어',
        required=False,
        widget=forms.NumberInput(
            attrs = {
                'class' : 'KMoCA',
                'placeholder':'단어 갯수 입력',
                'id' : 'KMoCA17'
            }
        ),
        #error_messages={'required': '갯수를 입력해주세요.'}
    )
    mc_abstraction_1 = forms.CharField(
        label='기차 - 비행기',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA18',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_abstraction_2 = forms.CharField(
        label='시계 - 저울',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA19',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_face = forms.CharField(
        label='얼굴',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA20',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_silks = forms.CharField(
        label='비단',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA21',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_school = forms.CharField(
        label='학교',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA22',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_pipe = forms.CharField(
        label='피리',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA23',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_yellow = forms.CharField(
        label='노랑',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA24',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )

    mc_de_1 = forms.IntegerField(
        label='범주형 단서 총점',
        required=False,
        widget=forms.NumberInput(
            attrs = {
                'class' : 'KMoCA',
                'placeholder':'총점 입력(0-5)',
                'id' : 'KMoCA25'
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    
    mc_de_2 = forms.IntegerField(
        label='선다형 단서 총점',
        required=False,
        widget=forms.NumberInput(
            attrs = {
                'class' : 'KMoCA',
                'placeholder':'총점 입력(0-5)',
                'id' : 'KMoCA26'
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )

    mc_date = forms.CharField(
        label='일',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA27',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_month = forms.CharField(
        label='월',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA28',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_year = forms.CharField(
        label='년',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA29',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_day = forms.CharField(
        label='요일',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA30',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_place = forms.CharField(
        label='장소',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA31',
                
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_city = forms.CharField(
        label='도시 이름',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA32',
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    ms_pentagon = forms.CharField(
        label='오각형 그리기',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMMSE',
                'id': 'KMMSE1',
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_score = forms.CharField(
        label='MC_Score',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class' : 'MC_Score',
                'placeholder' : '자동계산'
            }
        ),
        #error_messages={'required': '총점이 필요합니다.'}
    )

    class Meta:
        fields = [
            'id',
            'mc_atm',
            'mc_cube',
            'mc_clock_cont',
            'mc_clock_num',
            'mc_clock_hands',
            'mc_lion',
            'mc_bat',
            'mc_camel',
            'mc_re_1',
            'mc_re_2',
            'mc_forward',
            'mc_backward',
            'mc_vigilance',
            'mc_serial_7s',
            'mc_sentence_1',
            'mc_sentence_2',
            'mc_fluency',
            #'mc_fluency_N',
            'mc_abstraction_1',
            'mc_abstraction_2',
            'mc_face',
            'mc_silks',
            'mc_school',
            'mc_pipe',
            'mc_yellow',
            'mc_de_1',
            'mc_de_2',
            'mc_date',
            'mc_month',
            'mc_year',
            'mc_day',
            'mc_place',
            'mc_city',
            'ms_pentagon',
            'mc_score'
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        mc_atm= cleaned_data.get('mc_atm','')
        mc_cube= cleaned_data.get('mc_cube','')
        mc_clock_cont= cleaned_data.get('mc_clock_cont','')
        mc_clock_num= cleaned_data.get('mc_clock_num','')
        mc_clock_hands= cleaned_data.get('mc_clock_hands','')
        mc_lion= cleaned_data.get('mc_lion','')
        mc_bat= cleaned_data.get('mc_bat','')
        mc_camel= cleaned_data.get('mc_camel','')
        mc_re_1= cleaned_data.get('mc_re_1','')
        mc_re_2= cleaned_data.get('mc_re_2','')
        mc_forward = cleaned_data.get('mc_forward','')
        mc_backward = cleaned_data.get('mc_backward','')
        mc_vigilance = cleaned_data.get('mc_vigilance','')
        mc_serial_7s = cleaned_data.get('mc_serial_7s','')
        mc_sentence_1 = cleaned_data.get('mc_sentence_1','')
        mc_sentence_2 = cleaned_data.get('mc_sentence_2','')
        mc_fluency = cleaned_data.get('mc_fluency','')
        mc_abstraction_1 = cleaned_data.get('mc_abstraction_1','')
        mc_abstraction_2 = cleaned_data.get('mc_abstraction_2','')
        mc_face = cleaned_data.get('mc_face','')
        mc_silks = cleaned_data.get('mc_silks','')
        mc_school = cleaned_data.get('mc_school','')
        mc_pipe = cleaned_data.get('mc_pipe','')
        mc_yellow = cleaned_data.get('mc_yellow','')
        mc_de_1 = cleaned_data.get('mc_de_1','')
        mc_de_2 = cleaned_data.get('mc_de_2','')
        mc_date = cleaned_data.get('mc_date','')
        mc_month = cleaned_data.get('mc_month','')
        mc_year = cleaned_data.get('mc_year','')
        mc_day = cleaned_data.get('mc_day','')
        mc_place = cleaned_data.get('mc_place','')
        mc_city = cleaned_data.get('mc_city','')
        ms_pentagon = cleaned_data.get('ms_pentagon','')
        mc_score = cleaned_data.get('mc_score', '')
        

        KMoCAList = [mc_atm, mc_cube, mc_clock_cont,mc_clock_num,mc_clock_hands,mc_lion,mc_bat,mc_camel,mc_forward,mc_backward,mc_vigilance,mc_serial_7s,mc_sentence_1,mc_sentence_2,mc_fluency,mc_abstraction_1,mc_abstraction_2,mc_face,
                     mc_silks,mc_school,mc_pipe,mc_yellow,mc_date,mc_month,mc_year,mc_day,mc_place,mc_city,mc_score]
        if mc_fluency != '':
            mc_fluency_n = '1' if int(mc_fluency) >= 6 else '0'
        else:
            mc_fluency_n = ''
            
        kmoca_details = [mc_atm, mc_cube, mc_clock_cont,mc_clock_num,mc_clock_hands,mc_lion,mc_bat,mc_camel,mc_forward,mc_backward,mc_vigilance,mc_serial_7s,mc_sentence_1,mc_sentence_2,mc_fluency_n,mc_abstraction_1,mc_abstraction_2,mc_face,
                        mc_silks,mc_school,mc_pipe,mc_yellow,mc_date,mc_month,mc_year,mc_day,mc_place,mc_city]

        if (any('' == i for i in KMoCAList) and any(KMoCAList)):
            return self.add_error('mc_atm','모든 K-MoCA 항목을 입력해 주세요')
        elif (mc_score != '') and (sum(map(int, kmoca_details)) != int(mc_score)):
            return self.add_error('mc_score', 'K-MoCA 총점을 확인해주세요.')
        elif (mc_re_1!=None) and (int(mc_re_1)<0 or int(mc_re_1)>=6):
            return self.add_error('mc_re_1','K-MoCA 기억력 즉각회상 1차 점수를 확인해주세요.(0~5 숫자만 입력해주세요)')
        elif (mc_re_2!=None) and (int(mc_re_2)<0 or int(mc_re_2)>=6):
            return self.add_error('mc_re_2','K-MoCA 기억력 즉각회상 2차 점수를 확인해주세요.(0~5 숫자만 입력해주세요)')
        elif (mc_de_1!=None) and (int(mc_de_1)<0 or int(mc_de_1)>=6):
            return self.add_error('mc_de_1','K-MoCA 범주형 단서 총점을 확인해주세요.(0~5 숫자만 입력해주세요)')
        elif (mc_de_2!=None) and (int(mc_de_2)<0 or int(mc_de_2)>=6):
            return self.add_error('mc_de_2','K-MoCA 범주형 단서 총점을 확인해주세요.(0~5 숫자만 입력해주세요)')        
        else:
            self.mc_atm = mc_atm
            self.mc_cube = mc_cube
            self.mc_clock_cont = mc_clock_cont
            self.mc_clock_num = mc_clock_num
            self.mc_lion = mc_lion
            self.mc_bat = mc_bat
            self.mc_camel = mc_camel
            self.mc_re_1 = mc_re_1
            self.mc_re_2 = mc_re_2
            self.mc_forward = mc_forward
            self.mc_backward = mc_backward
            self.mc_vigilance = mc_vigilance
            self.mc_serial_7s = mc_serial_7s
            self.mc_sentence_1 = mc_sentence_1
            self.mc_sentence_2 = mc_sentence_2
            self.mc_fluency = mc_fluency
            self.mc_abstraction_1 = mc_abstraction_1
            self.mc_abstraction_2 = mc_abstraction_2
            self.mc_face = mc_face
            self.mc_silks = mc_silks
            self.mc_school = mc_school
            self.mc_pipe = mc_pipe
            self.mc_yellow = mc_yellow
            self.mc_de_1 = mc_de_1
            self.mc_de_2 = mc_de_2
            self.mc_date = mc_date
            self.mc_month = mc_month
            self.mc_year = mc_year
            self.mc_day = mc_day
            self.mc_place = mc_place
            self.mc_city = mc_city
            self.ms_pentagon=ms_pentagon
            self.mc_score = mc_score