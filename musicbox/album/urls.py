from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'album'

urlpatterns = [
                path('', albums_list, name='list'),
                path('upload/', upload_album, name='upload'),
                path('<int:id>/update/', album_update, name='update'),
                path('<int:id>/delete/', album_delete, name='delete'),
                path('<int:album_id>/', album_detail, name='detail'),
                path('search/<str:query>/', search, name='search'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)