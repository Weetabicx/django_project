from .views import *
from django.urls import path, re_path

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),

]