from django.urls import path
from .views import *

app_name = 'song'

urlpatterns = [
    path('', song_list_view, name='song_list'),
    path('songs/delete/<int:song_id>/', delete_song, name='delete_song'),
    path('song/upload_song',upload_song, name='upload_song'),
    path('songs/<int:song_id>/', song_detail_view, name='song_detail'),
    path('songs/update/<int:song_id>/', update_song, name='update_song'),
    path('songs/add-comment/<int:song_id>/', add_comment_to_song, name='add_comment'),
]
