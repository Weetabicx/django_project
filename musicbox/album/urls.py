from django.urls import path
from .views import *

urlpatterns = [
    path('', albums_list, name='albums_list'),

]

