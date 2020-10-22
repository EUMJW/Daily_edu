"""mysite URL Configuration

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
from app1_hello import views
from home import home_views
from app2_template import  template_views
from app3_database import database_views
urlpatterns = [
    path('', home_views.home_index),
    path('admin/', admin.site.urls),
    path('app1_hello/',views.index),
    path('app2_template/',template_views.index),
    path('app3_database/',database_views.index),
]
