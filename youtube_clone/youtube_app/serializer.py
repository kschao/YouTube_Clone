from django.db import models
from rest_framework import serializers
from .models import Channel, Comment, Reply, Video

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'video_id', 'body', 'likes', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['comment', 'body']
        
class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ['title', 'description', 'path', 'datetime', 'user']
        
class ChannelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Channel
        fields = ['channel_name', 'subscribers', 'user']