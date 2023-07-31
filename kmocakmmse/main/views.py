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
    
    return render(request, 'main/home.html', context)

def info(request):
        return render(request, 'main/info.html')
    
def details(request):
    kmoca_form = KMoCAForm()
    context = {'mocaform': kmoca_form}
    
    # 환자정보 입력 여부 체크
    if request.session['info']:
        p_id = request.session.get('p_id','')
    else:
        p_id = None

    if request.method == 'GET':
        return render(request, 'main/details.html', context)
    
    elif request.method == 'POST':
        kmoca_form = KMoCAForm(request.POST)
        if (kmoca_form.is_valid()):
            now_date = timezone.now()
            
            if (kmoca_form.mc_score == ''):
                kmoca_form.add_error('mc_score', '검사를 시행해주세요.')
                context['mocaform']=kmoca_form
                return render(request, 'main/details.html', context)

            # K-MoCA
            if kmoca_form.mc_score != '':
                kmoca_data = kmoca_form.save(commit=False)
                kmoca_data.moca_mocak = '0'
                kmoca_data.input_date = now_date
                kmoca_data.mc_fluency_n = '1' if int(kmoca_form.mc_fluency) >= 6 else '0'
                kmoca_data.save()
            return redirect('output:machin')
                    
        else:
            context['mocaform'] = kmoca_form
            if kmoca_form.errors:
                for value in kmoca_form.errors.values():
                    context['error'] = value
        return render(request, 'main/details.html', context)