from django.contrib import admin
from .models import TopicModel, ContentModel

# Register your models here.
admin.site.register(TopicModel)
admin.site.register(ContentModel)