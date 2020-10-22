from django.db import models

# Create your models here.
# home/models.py

class TopicModel(models.Model) :
    topic_idx = models.AutoField(primary_key=True)
    topic_name = models.TextField(null=False)

class ContentModel(models.Model) :
    content_idx = models.AutoField(primary_key=True)
    content_topic_idx = models.ForeignKey(TopicModel, null=True, on_delete=models.CASCADE)
    content_text = models.TextField(null=False)