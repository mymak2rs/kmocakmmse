from django.urls import path
from main import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name='info'),
    path('interpretation/', views.interpretation, name='interpretation'),
]

