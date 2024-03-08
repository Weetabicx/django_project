from django.urls import path
from .views import *

urlpatterns = [
    path('', song_list_view, name='song_list'),
    path('upload_song/',  upload_song, name='upload_song'),
    path('delete/<int:song_id>/', delete_song, name='delete_song'),

]
