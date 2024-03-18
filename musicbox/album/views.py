from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumForm, AlbumCommentForm
from django.contrib.auth.decorators import login_required
from .models import Album,Album_Comment
from song.models import Song


# Create your views here.

def albums_list(request):
    albums = Album.objects.all()
    return render(request, 'album/albums_list.html', {'albums': albums})

def upload_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums_list')
    else:
        form = AlbumForm()
    return render(request, 'album/upload_album.html', {'form': form})

def album_update(request, id):
    album = get_object_or_404(Album, id=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('albums_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album/album_form.html', {'form': form})

def album_delete(request, id):
    album = get_object_or_404(Album, id=id)
    album.delete()
    return redirect('albums_list')


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    comments = Album_Comment.objects.filter(album=album)  # 获取专辑的所有评论

    if request.method == 'POST':
        comment_form = AlbumCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.album = album  # 将新评论与当前专辑关联
            new_comment.save()
            return redirect('album_detail', album_id=album.id)  # 重定向回专辑详情页
    else:
        comment_form = AlbumCommentForm()

    return render(request, 'album/album_detail.html', {
        'album': album,
        'comments': comments,
        'comment_form': comment_form
    })