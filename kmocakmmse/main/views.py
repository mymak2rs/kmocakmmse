from django.shortcuts import render

# 404 page custom
def page_not_found_view(request, exception):
    return render(request, 'main/404.html', status=404)


def home(request, context={}):
    request.session['first'] = False
    request.session['register'] = False
    request.session['info'] = False
    request.session['upload'] = False
    
    request.session['p_id'] = False

    login_session = request.session.get('login_session', '')
    
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True

    return render(request, 'main/home.html', context)