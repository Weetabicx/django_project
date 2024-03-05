from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('', index, name='index'),
]
