"""MiniProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import home.views
import topic.views
import content.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.index),
    path('topic/', topic.views.index),
    path('topic/add_topic/', topic.views.add_topic),
    # 요청 주소 중 content/값 에서 값 부분에 들어오는 값을 index 함수의
    # content_topic_idx 매개변수에 담아준다.
    path('content/<int:content_topic_idx>', content.views.index),
    path('topic/add_topic_pro/', topic.views.add_topic_pro),
    path('content/add_content_pro', content.views.add_content_pro)
]









