from .views import *
from django.urls import path, re_path

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('manage_account/', manage_account, name='manage_account'),
    path('search/', search, name='search'),
    path('profile/', user_profile, name='user_profile'),
    ]