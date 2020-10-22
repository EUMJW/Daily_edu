from django.shortcuts import render
from home import models
from django.http import HttpResponse

# Create your views here.
def index(request, content_topic_idx):
    # filter 함수 : where 컬럼명=값 에 해당한다.
    topic_model = models.TopicModel.objects.filter(topic_idx=content_topic_idx)

    # 토론방에 해당하는 데이터를 가져온다.
    content_list = models.ContentModel.objects.filter(content_topic_idx=content_topic_idx)\
        .order_by('content_idx')

    data_dic = {
        'topic_model' : topic_model,
        'content_topic_idx' : content_topic_idx,
        'content_list' : content_list
    }

    return render(request, 'content/index.html', data_dic)

def add_content_pro(request) :
    # 데이터를 추출한다.
    content_topic_idx = request.POST.get('content_topic_idx', None)
    content_text = request.POST.get('content_text', None)

    # print(content_topic_idx)
    # print(content_text)

    # content_topic_idx에 해당하는 TopicModel 객체를 생성한다.
    topic_model = models.TopicModel(topic_idx=content_topic_idx)

    content_model = models.ContentModel(content_topic_idx=topic_model, content_text=content_text)
    content_model.save()
    
    return HttpResponse(f'''
                        <script>
                            alert('저장되었습니다')
                            location.href='/content/{content_topic_idx}'
                        </script>
                        ''')








