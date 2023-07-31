from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import PatientForm, KMoCAForm
from .module import check


# 404 page custom
def page_not_found_view(request, exception):
    return render(request, 'main/404.html', status=404)


def home(request, context={}):
    request.session['first'] = False
    request.session['info'] = False
    request.session['re_input'] = False
    
    return render(request, 'main/home.html', context)

def info(request):
    if request.session['re_input']:
        print(request.session['re_input'])
        patient_info = request.session.get('patient_info')
        
        if patient_info['education'] != 0.0 and patient_info['education'] != 0.5:
            patient_info['education'] = 999.0
        
        request.session['re_input'] = False 
        context = {'forms': PatientForm(initial=patient_info)}
        return render(request, 'main/info.html', context)
    else:
        patient_form = PatientForm()
    
    edu = request.session.get('edu', '')
    context = {'forms': patient_form, 'edu1': edu, 'first': True }
        
    if request.method == 'GET':
        return render(request, 'main/info.html', context)
    
    elif request.method == 'POST':
        patient_form = PatientForm(request.POST)
        edu = request.POST.get('edu_input')
        request.session['edu'] = edu
        # 데이터의 유효성을 검사하는 메소드, form.py에서 작성한 clean() 메소드 호출, 유효성 검사가 ok이면 true
        if patient_form.is_valid():                           
            if patient_form.education == 999:
                patient_form.education = edu
                
            if 'cutoff' in request.POST:
                if patient_form.kmoca_total == None:
                    patient_form.add_error('kmoca_total', '하나라도 값을 입력해주세요.')
                    context['forms'] = patient_form
                    context['error'] = True
                    return render(request, 'main/info.html', context)

                request.session['info'] = True
                request.session['cutoff'] = True
                request.session['details'] = False 
                
                patient_info = patient_form.cleaned_data
                request.session['patient_info'] = patient_info
                      
                return redirect('myapp:confirm')

            else:
                request.session['info'] = True
                request.session['cutoff'] = False
                request.session['details'] = True
                
                return redirect('myapp:confirm')

        else:   # error 전달
            context['forms'] = patient_form
            if patient_form.errors:
                for value in patient_form.errors.values():
                    context['error'] = value
        return render(request, 'main/info.html', context)


def confirm(request, patient_info={}):
     # 환자정보 입력 여부 체크
    if request.session['info']:
        p_id = request.session.get('info_id','')
    else:
        p_id = None
            
    patient_info = request.session.get('patient_info')
    context = {
                'num': patient_info['patient_no'],
                'sex': check.check_answer(patient_info['sex']),
                'age': patient_info['age'],
                'edu': check.check_answer(patient_info['education']),
                'KMoCA': check.check_answer(patient_info['kmoca_total']),
                'hand': check.check_answer(patient_info['handedness']),
                'patient_cog': check.check_answer(patient_info['patient_cog_compl']),
                'caregiver_cog': check.check_answer(patient_info['caregiver_cog_compl']),
                'nuer_prob': check.check_answer(patient_info['neurologic_problems']),
                'parkin_dis': check.check_answer(patient_info['parkinson_disease']),
                'dia_duration': check.check_answer(patient_info['diag_duration']),
                'depression': check.check_answer(patient_info['depression']),
                'sgds_bdi': check.check_answer(patient_info['sgds_bdi_depression']),
                'HY': check.check_answer(patient_info['hy_stage']),
                'UPDRS': check.check_answer(patient_info['motor_updrs_score']),
                'SGDS': check.check_answer(patient_info['sgds_score']),
            }
    
    if request.method == 'GET':
        return render(request, 'main/confirm.html', context)
    
    elif request.method == 'POST':
        if 'save' in request.POST:
            request.session['info_id'] = None
            request.session['edu'] = None
            if request.session['cutoff']:
                return redirect('myapp:cutoff')
            else:
                return redirect('myapp:details')
        
        elif 'cancel' in request.POST:
            # 삭제 전에 가져와서 다시 info 페이지에 넣어준다?
            request.session['re_input'] = True
            return redirect('myapp:info')
        return render(request, 'main/info.html')
    
def details(request):
    kmoca_form = KMoCAForm()
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

            return redirect('output:machin')
                    
        else:
            context['mocaform'] = kmoca_form
            if kmoca_form.errors:
                for value in kmoca_form.errors.values():
                    context['error'] = value
        return render(request, 'main/details.html', context)
