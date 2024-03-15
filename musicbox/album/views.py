from django.shortcuts import render

# Create your views here.
def albums_list(request):
    return render(request, 'album/albums_list.html')