from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 주소만 입력하고 들어왔을 때 호ㅜㄹ될 함수
def index(request):
    return HttpResponse('<h1>Hello World</h1>')