from django.urls import path
from .views import *

app_name = 'song'

urlpatterns = [
    path('', song_list_view, name='list'),
    path('<int:song_id>/delete/', delete_song, name='delete'),
    path('upload', upload_song, name='upload'),
    path('<int:song_id>/', song_detail_view, name='details'),
    path('<int:song_id>/update/', update_song, name='update'),
    path('<int:song_id>/add-comment', add_comment_to_song, name='add-comment'),
]
