import pandas as pd
import numpy as np
from django.shortcuts import render, redirect
from .forms import PatientForm, KMoCAForm
from .module import check, cutoff_norm
from .regression import model
from django.http import HttpResponseNotFound

# 404 page custom
def page_not_found_view(request, exception=None):
    return render(request, 'main/404.html', status=404)


def home(request, context={}):
    request.session['info'] = False
    request.session['re_input'] = False
    request.session['details'] = False
    request.session['patient_info'] = None
    request.session['kmoca'] = None
    
    if request.method == 'GET':
        return render(request, 'main/home.html', context)
    
    elif request.method == 'POST':
        if 'cutoff' in request.POST:
            request.session['cutoff'] = True
            request.session['machine'] = False
        else:
            request.session['cutoff'] = False
            request.session['machine'] = True
            
        return redirect('myapp:info')
    
    

def info(request):
    patient_form = PatientForm()
    cutoff = request.session.get('cutoff', '')
    machine = request.session.get('machine', '')
    context = {'forms': patient_form, 'cutoff': cutoff, 'machine': machine }

        
    if request.method == 'GET':
        if cutoff:
            return render(request, 'main/info_cutoff.html', context)
        else:
            return render(request, 'main/info.html', context)
    
    elif request.method == 'POST':
        patient_form = PatientForm(request.POST)
        edu = request.POST.get('edu_input')
        request.session['edu'] = edu
        
        # 데이터의 유효성을 검사하는 메소드, form.py에서 작성한 clean() 메소드 호출, 유효성 검사가 ok이면 true
        if patient_form.is_valid():                           
            if patient_form.education == 999.0:
                patient_form.education = edu
                
            if cutoff:
                if patient_form.kmoca_total == None:
                    patient_form.add_error('kmoca_total', '하나라도 값을 입력해주세요.')
                    context['forms'] = patient_form
                    context['error'] = True
                    return render(request, 'main/info.html', context)

                request.session['info'] = True
                
                patient_info = patient_form.cleaned_data
                if patient_info['education'] == 999.0:
                    patient_info['education'] = edu
                request.session['patient_info'] = patient_info
                      
                return redirect('myapp:interpretation')

            else:
                
                patient_info = patient_form.cleaned_data
                if patient_info['education'] == 999.0:
                    patient_info['education'] = edu
                request.session['patient_info'] = patient_info
                
                return redirect('myapp:confirm')

        else:   # error 전달
            context['forms'] = patient_form
            if patient_form.errors:
                for value in patient_form.errors.values():
                    context['error'] = value
        return render(request, 'main/info.html', context)


def details(request):
    kmoca_form = KMoCAForm()
    patient_info = request.session.get('patient_info')
    context = {'mocaform': kmoca_form}

    if request.method == 'GET':
        return render(request, 'main/details.html', context)
    
    elif request.method == 'POST':
        kmoca_form = KMoCAForm(request.POST)
        if (kmoca_form.is_valid()):
            
            if (kmoca_form.mc_score == ''):
                kmoca_form.add_error('mc_score', '검사를 시행해주세요.')
                context['mocaform']=kmoca_form
                return render(request, 'main/details.html', context)

            if patient_info['kmoca_total']:
                if int(kmoca_form.mc_score) != patient_info['kmoca_total']:
                    kmoca_form.add_error('mc_score', 'K-MoCA 총점이 다릅니다.')
                    context['mocaform']=kmoca_form
                    return render(request, 'main/details.html', context)
            
            kmoca = kmoca_form.cleaned_data
            request.session['kmoca'] = kmoca
            request.session['details'] = True
            return redirect('myapp:interpretation')
                    
        else:
            context['mocaform'] = kmoca_form
            if kmoca_form.errors:
                for value in kmoca_form.errors.values():
                    context['error'] = value
        return render(request, 'main/details.html', context)

def interpretation(request):
    # 데이터 불러오기
    patient_info = request.session.get('patient_info')
    kmoca = request.session.get('kmoca')
    
    if patient_info is None:
        return render(request, 'main/interpretation.html')
    
    if kmoca is None:
        return render(request, 'main/interpretation.html')
    
    # 데이터 전처리
    patient_info['sex'] = check.char2int(patient_info['sex'])
    kmoca['mc_fluency'] = 1 if int(kmoca['mc_fluency']) >= 6 else 0
    
    info_df = pd.DataFrame.from_dict(data=patient_info, orient='index').transpose()
    kmoca_df = pd.DataFrame.from_dict(data=kmoca, orient='index').transpose()
    
    moca_data = [info_df.sex, info_df.age, info_df.education, info_df.patient_cog_compl, info_df.caregiver_cog_compl, 
                info_df.diag_duration, info_df.hy_stage, info_df.motor_updrs_score, info_df.sgds_bdi_depression
                ]
    
    vssp = np.sum(list(map(int,[kmoca_df.mc_atm, kmoca_df.mc_cube, kmoca_df.mc_clock_cont, kmoca_df.mc_clock_num, kmoca_df.mc_clock_hands])))
    name = np.sum(list(map(int,[kmoca_df.mc_lion, kmoca_df.mc_bat, kmoca_df.mc_camel])))
    attention = np.sum(list(map(int, [kmoca_df.mc_forward,kmoca_df.mc_backward, kmoca_df.mc_vigilance, kmoca_df.mc_serial_7s])))
    language = np.sum(list(map(int, [kmoca_df.mc_sentence_1, kmoca_df.mc_sentence_2, kmoca_df.mc_fluency])))
    abstraction = np.sum(list(map(int, [kmoca_df.mc_abstraction_1, kmoca_df.mc_abstraction_2])))
    memory = np.sum(list(map(int, [kmoca_df.mc_face, kmoca_df.mc_silks, kmoca_df.mc_school, kmoca_df.mc_pipe, kmoca_df.mc_yellow])))
    orientation = np.sum(list(map(int, [kmoca_df.mc_date, kmoca_df.mc_month,kmoca_df.mc_year, kmoca_df.mc_day, kmoca_df.mc_place, kmoca_df.mc_city])))

    # model 예측
    moca_data.extend([vssp, name, attention, language, abstraction, memory, orientation, kmoca_df.ms_pentagon])
    moca_data = np.array([moca_data], dtype=float)
    
    mocab_machin_result = model.mocab_LR(moca_data)[1]
    mocad_machin_result = model.mocad_LR(moca_data)[1]
    
    age = int(info_df.age)
    edu = int(info_df.education)
    moca_score = int(kmoca_df.mc_score)
    
    cutoff_moca, moca_zscore = cutoff_norm.MoCA_cutoff(age, edu, moca_score)
    
    context = {
                'age': age,
                'edu': edu,
                'KMoCA': moca_score,
                'pentagon': 'pass' if int(kmoca_df.ms_pentagon) == 1 else 'fail',
                'moca_cutoff': int(cutoff_moca),
                'mocab_machin_result': str(mocab_machin_result) if kmoca else '',
                'mocad_machin_result': str(mocad_machin_result) if kmoca else '',
                'mocab_machin_decision': False,
                'mocad_machin_decision': False
               }
    
    if cutoff_moca > moca_score:
        context['cutoff_result'] = True
    else:
        context['cutoff_result'] = False
    
    if mocab_machin_result > 50:
        context['mocab_machin_decision'] = True
    if mocad_machin_result > 50:
        context['mocad_machin_decision'] = True
    
    return render(request, 'main/interpretation.html', context)