from django.shortcuts import render
from .models import Comment, Reply, Video, Channel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CommentSerializer, ReplySerializer, VideoSerializer, ChannelSerializer
from django.http import Http404



# Create your views here.
class VideoPage(APIView):
    
    def get(self, request):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentSection(APIView):
    
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
            comment = self.get_object(pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReplySection(APIView):
    
    def get(self, request):
        comment = Reply.objects.all()
        serializer = ReplySerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
            Reply = self.get_object(pk)
            Reply.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
class ChannelSection(APIView):
    
    def get(self, request):
        comment = Channel.objects.all()
        serializer = ChannelSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
            Channel = self.get_object(pk)
            Channel.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)