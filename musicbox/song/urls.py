from django.urls import path
from .views import *

app_name = 'song'

urlpatterns = [
    path('', song_list_view, name='list'),
    path('upload_song/',  upload_song, name='upload'),
    path('delete/<int:song_id>/', delete_song, name='delete'),


]
