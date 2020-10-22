from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#첫페이지
def home_index(request):
    # return HttpResponse('<h1>Home Index</h1>')
    return render(request, 'home/index.html')