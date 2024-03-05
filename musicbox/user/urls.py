from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('manage_account/', manage_account, name='manage account')

]
