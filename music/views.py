from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
def IndexView(request):
    return render(request, 'music/index.html')

def LoadMoreAPI(request):
    html_code = render_to_string('music/load-more.html')
    return JsonResponse({'html': html_code})