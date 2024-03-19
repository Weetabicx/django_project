from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', albums_list, name='albums_list'),
                  path('albums_list',  albums_list, name='albums_list'),
                  path('upload_album/', upload_album, name='upload_album'),
                  path('album/<int:id>/update/', album_update, name='album_update'),
                  path('albums/<int:album_id>/delete/', views.delete_album, name='delete_album'),
                  path('albums/<int:album_id>/', album_detail, name='album_detail'),
                  path('albums/<int:album_id>/', views.album_detail, name='album_detail'),
                  path('albums/<int:album_id>/edit/', views.edit_album, name='edit_album'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)