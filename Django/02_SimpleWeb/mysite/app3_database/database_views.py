from django.shortcuts import render
from django.http import HttpResponse
from .models import TestClass



# Create your views here.
def index(request):
    # 모델 객체를 생성한다.
    # 이 때 저장할 데이터도 셋팅한다.
    # test_model = TestClass(test_str='문자열1', test_int=100)
    #
    # test_model = TestClass(test_str='문자열2',test_int=200)
    # test_model.save()
    # print(test_model.sql)

    # 데이터를 가져온다.
    test_list = TestClass.objects.all()
    print(test_list)
    print(test_list.query)
    print(test_list.values())


    data_dic = {
            'test_list' : test_list
    }

    return render(request, 'app3_database/database.html', data_dic)
