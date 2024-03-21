from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'album'

urlpatterns = [
                path('', albums_list, name='list'),
                path('upload/', upload_album, name='upload'),
                path('<int:album_id>/edit/', edit_album, name='edit'),
                path('<int:album_id>/delete/', delete_album, name='delete'),
                path('<int:album_id>/', album_detail, name='details'),
                path('search/', search_albums, name='search'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)