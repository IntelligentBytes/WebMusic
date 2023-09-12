from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from music import models

# Create your views here.
def IndexView(request):
    musics = models.Music.objects.all()
    return render(request, 'music/index.html', {'musics': musics})

def LoadMoreAPI(request):
    musics = models.Music.objects.all()
    html_code = render_to_string('music/load-more.html', {'musics': musics})
    return JsonResponse({'html': html_code})