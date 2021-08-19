from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.VideoPage.as_view()),
    path('comments/', views.CommentSection.as_view()),
    path('reply/', views.ReplySection.as_view()),
    path('channel/', views.ChannelSection.as_view()),
]