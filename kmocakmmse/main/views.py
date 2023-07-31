from django.shortcuts import render

# 404 page custom
def page_not_found_view(request, exception):
    return render(request, 'main/404.html', status=404)


def home(request, context={}):
    request.session['first'] = False
    request.session['info'] = False
    
    return render(request, 'main/home.html', context)

def info(request):
        return render(request, 'main/info.html')
    