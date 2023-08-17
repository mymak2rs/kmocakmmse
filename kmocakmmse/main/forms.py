from typing import Any, Mapping, Optional, Type, Union
from django import forms
from django.forms.utils import ErrorList
import main.module.choice as choice
from django.utils.safestring import mark_safe

class PatientForm(forms.Form):    
    sex = forms.CharField(
        label='Sex',
        required=False,
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
        label='Age (years old)',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'age',
                'placeholder': '00 years old',
                'id': 'age'
            }
        ),
        error_messages={'required': 'Please input your age.'}
    )

    education = forms.FloatField(
        label='Years in Education (years)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_EDU,
            attrs={
                'class': 'edu',
                'id': 'edu'
            }
        ),
        error_messages={'required': 'Please input your education.'}
    )

    edu_input = forms.FloatField(
        label='',
        required=False,
        widget=forms.NumberInput(
            attrs={'placeholder': '00 years'}
        )
    )

    kmoca_total = forms.IntegerField(
        label='MoCA score',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'kmoca_total',
                'placeholder': 'K-MoCA score',
                'id': 'kmoca_total'
            }
        )
    )
    patient_cog_compl = forms.CharField(
        label='Does a patient complain memory decline?',
        required=False,
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
        label='Do caregivers complain memory decline of a patient?',
        required=False,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_YES_NO,
            attrs={
                'class': 'care_cog',
                'id': 'care_cog'
            }
        ),
        error_messages={'required': '보호자의 환자 기억력 저하 여부를 선택해주세요.'}
    )
    diag_duration = forms.FloatField(
        label='Duration of Parkinson’s disease (months)',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'dia_duration',
                'placeholder': '00 months',
                'id': 'dia_duration'
            }
        )
    )
    sgds_bdi_depression = forms.CharField(
        label='Has a patient been diagnosed with depression?',
        required=False,
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
         label='Hoehn & Yahr stage',
        required=False,
        widget=forms.Select(
            choices=choice.CHOICE_HY,
            attrs={
                'class': 'hy',
                'placeholder': 'H&Y stage',
                'id': 'hy'
            }
        )
    )
    motor_updrs_score = forms.IntegerField(
        label='Score of part III (motor evaluation) of Unified Parkinson’s Disease Rating Scale (UPDRS)',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'updrs',
                'placeholder': 'Motor UPDRS score',
                'id': 'updrs'
            }
        )
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':'The field is required'}

    class Meta:
        fields = [
            'sex',
            'age',
            'education',
            'edu_input',
            'patient_cog_compl',
            'caregiver_cog_compl',
            'neurologic_problems',
            'diag_duration',
            'sgds_bdi_depression',
            'hy_stage',
            'motor_updrs_score',
            'kmoca_total',
        ]


    def clean(self):
        cleaned_data = super().clean()
        sex = cleaned_data.get('sex', '')
        age = cleaned_data.get('age', '')
        education = cleaned_data.get('education', '')
        edu_input = cleaned_data.get('edu_input', '')
        kmoca_total = cleaned_data.get('kmoca_total', '')
        patient_cog_compl = cleaned_data.get('patient_cog_compl', '')
        caregiver_cog_compl = cleaned_data.get('caregiver_cog_compl', '')
        neurologic_problems = cleaned_data.get('neurologic_problems', '')
        diag_duration = cleaned_data.get('diag_duration', '')
        sgds_bdi_depression = cleaned_data.get('sgds_bdi_depression', '')
        depression = cleaned_data.get('depression', '')
        hy_stage = cleaned_data.get('hy_stage','')
        motor_updrs_score = cleaned_data.get('motor_updrs_score','')

        if (education == 999) and (edu_input == None):
            return self.add_error('edu_input', 'Please input your education.')
                    
        if (diag_duration != None) and (age < diag_duration/12):
            return self.add_error('age', '나이가 유병기간보다 적습니다.')
    
        if (diag_duration != None) and (diag_duration < 1):
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
        
        if (motor_updrs_score != None) and (motor_updrs_score < 0 or motor_updrs_score > 200):
            return self.add_error('motor_updrs_score', 'Motor UPDRS 점수를 확인해주세요.')

        if (kmoca_total != None) and (kmoca_total > 30) | (kmoca_total < 0):
            return self.add_error('kmoca_total', 'MoCA score must be less than or equal to 30.')
    
        
        self.sex = sex
        self.age = age
        self.education = education        
        self.edu_input = edu_input
        self.patient_cog_compl = patient_cog_compl
        self.caregiver_cog_compl = caregiver_cog_compl
        self.neurologic_problems = neurologic_problems
        self.diag_duration = diag_duration
        self.depression = depression
        self.sgds_bdi_depression = sgds_bdi_depression
        self.hy_stage = hy_stage
        self.motor_updrs_score = motor_updrs_score
        self.kmoca_total = kmoca_total
        
        
class KMoCAForm(forms.Form):
    mc_atm = forms.CharField(
        label='Trail Making Test',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA1',
                'name': 'KMoCA1'
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_cube = forms.CharField(
        label='Wired cube copy',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA2',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_clock_cont = forms.CharField(
        label='Draw clock (contour)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA3',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_clock_num = forms.CharField(
        label='Draw clock (numbers)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA4',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_clock_hands = forms.CharField(
        label='Draw clock (hands)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA5',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_lion = forms.CharField(
        label='Lion',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA6',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_bat = forms.CharField(
        label='Rhino (박쥐)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA7',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_camel = forms.CharField(
        label='Camel',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA8',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )

    mc_re_1 = forms.IntegerField(
        label='1st trial',
        required=False,
        widget=forms.NumberInput(
            attrs = {
                'class' : 'KMoCA',
                'placeholder':'input score (0-5)',
                'id' : 'KMoCA9'
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )    
    
    mc_re_2 = forms.IntegerField(
        label='2nd trial',
        required=False,
        widget=forms.NumberInput(
            attrs = {
                'class' : 'KMoCA',
                'placeholder':'input score (0-5)',
                'id' : 'KMoCA10'
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    ) 

    mc_forward = forms.CharField(
        label='digit span forward',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA11',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_backward = forms.CharField(
        label='digit span backward',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA12',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_vigilance = forms.CharField(
        label='Tap with hands at each letter',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA13',
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_serial_7s = forms.CharField(
        label='Serial 7',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_MOCA12_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA14',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_sentence_1 = forms.CharField(
        label='repetition 1 (칼날같이...)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA15',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_sentence_2 = forms.CharField(
        label='repetition 2  (스물 일곱...)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA16',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_fluency = forms.CharField(
        label= mark_safe('Verbal fluency (Number of words) <br> ("ㄱ"으로 시작하는 단어)'),
        required=True,
        widget=forms.NumberInput(
            attrs = {
                'class' : 'KMoCA',
                'placeholder':'Number of words',
                'id' : 'KMoCA17'
            }
        ),
        error_messages={'required': '갯수를 입력해주세요.'}
    )
    mc_abstraction_1 = forms.CharField(
        label='train-bicycle (기차 - 비행기)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA18',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_abstraction_2 = forms.CharField(
        label='watch-ruler (시계 - 저울)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA19',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_face = forms.CharField(
        label='Face (얼굴)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA20',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_silks = forms.CharField(
        label='Velvet (비단)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA21',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_school = forms.CharField(
        label='Church (학교)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA22',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_pipe = forms.CharField(
        label='Daisy (피리)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA23',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_yellow = forms.CharField(
        label='Red (노랑)',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA24',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )

    mc_de_1 = forms.IntegerField(
        label='Recall score: Cued recall',
        required=False,
        widget=forms.NumberInput(
            attrs = {
                'class' : 'KMoCA',
                'placeholder':'input score (0-5)',
                'id' : 'KMoCA25'
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )
    
    mc_de_2 = forms.IntegerField(
        label='Recall score: Multiple choice',
        required=False,
        widget=forms.NumberInput(
            attrs = {
                'class' : 'KMoCA',
                'placeholder':'input score (0-5)',
                'id' : 'KMoCA26'
            }
        ),
        #error_messages={'required': '점수를 선택해주세요.'}
    )

    mc_date = forms.CharField(
        label='date',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA27',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_month = forms.CharField(
        label='month',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA28',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_year = forms.CharField(
        label='year',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA29',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_day = forms.CharField(
        label='day',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA30',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_place = forms.CharField(
        label='place',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA31',
                
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_city = forms.CharField(
        label='city',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_SCORE,
            attrs={
                'class': 'KMoCA',
                'id': 'KMoCA32',
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    ms_pentagon = forms.CharField(
        label='Pentagon drawing',
        required=True,
        widget=forms.RadioSelect(
            choices=choice.CHOICE_PENTAGON,
            attrs={
                'class': 'KMMSE',
                'id': 'KMMSE1',
            }
        ),
        error_messages={'required': '점수를 선택해주세요.'}
    )
    mc_score = forms.CharField(
        label='MC_Score',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class' : 'MC_Score',
                'placeholder' : 'Auto'
            }
        ),
        error_messages={'required': '총점이 필요합니다.'}
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
                     mc_silks,mc_school,mc_pipe,mc_yellow,mc_date,mc_month,mc_year,mc_day,mc_place,mc_city,mc_score, ms_pentagon]
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