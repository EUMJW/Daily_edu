from django.shortcuts import render

# Create your views here.

def index(request):
    #html 파일을 가지고 응답결과를 만들 때 사용할 데이터
    data_dic = {
        'a1' : 100,
        'a2' : 11.11,
        'a3' : True,
        'a4' : '안녕하세요',
        'a5' : [10,20,30,40,50],
        'a6' : {'key1' : 100, 'key2' : 200}
    }
    return render(request, 'app2/index.html', data_dic)
