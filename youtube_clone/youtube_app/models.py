from django.db import models
from django.db.models.expressions import F

# Create your models here.
class Comment(models.Model):
    video_id = models.CharField(max_length=50)
    body = models.CharField(max_length=250)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=250)
    
class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    path = models.CharField(max_length=70)
    dattime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    
class Channel(models.Model):
    channel_name = models.CharField(max_length=50, blank=False, null=False)
    subscribers = models.IntegerField(default=0, blank=False, null=False)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)