from django.shortcuts import render
from django.http import HttpResponse
from home import models
from django.db.models import Count

# Create your views here.
def index(request) :
    # all : select 문
    # order_by : order by문. -를 붙히면 내림차순 정렬
    topic_list = models.TopicModel.objects.all().order_by('-topic_idx')
    # print(topic_list)
    # print(topic_list.query)
    # print(topic_list.values())

    # test = models.ContentModel.objects.all().values('content_topic_idx').annotate(cnt=Count('content_text'))
    # for obj in test :
    #     print(obj)

    # 외래키 관계인 경우 : 모델 변수의 이름을 넣어주면 값을 가져오고
    # 모델 변수이름__ 를 하면 외래키관계로 참조하고 있는 모델의 데이터를 가져올 수 있다.
    topic_list2 = models.ContentModel.objects.select_related()\
        .values('content_topic_idx', 'content_topic_idx__topic_name')\
        .annotate(content_cnt=Count('content_text')).order_by('-content_topic_idx')

    print(topic_list2)

    for obj in topic_list2 :
        print(obj)

    data_dic = {
        'topic_list' : topic_list2
    }

    return render(request, 'topic/index.html', data_dic)

def add_topic(request) :
    return render(request, 'topic/add_topic.html')

def add_topic_pro(request) :
    # 전달받은 데이터를 추출한다.
    topic_name = request.POST.get('topic_name', None)
    # 저장
    topic_model = models.TopicModel(topic_name=topic_name)
    topic_model.save()

    return HttpResponse('''
                        <script>
                            alert('저장되었습니다')
                            location.href = '/topic'
                        </script>
                        ''')













