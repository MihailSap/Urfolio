from django.contrib import admin
from django.urls import path, include
from . import views
from .views import (
    ProjectListView, ProjectCreateView,
    ProjectDetailView, ProjectUpdateView,
    ProjectDeleteView, LikeView, comment_sent,
    comment_delete_view, reply_sent,
    reply_delete_view, like_project,
)

app_name = 'projects'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<pk>/like/', like_project, name='like-project'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('new/', ProjectCreateView.as_view(), name='project_create'),

    path('like/<int:pk>', LikeView, name='like_project'),

    path('commentsent/<int:pk>', comment_sent, name='comment-sent'),
    path('comment/delete/<pk>', comment_delete_view, name='comment-delete'),
    path('reply-sent/<pk>', reply_sent, name='reply-sent'),
    path('reply/delete/<pk>', reply_delete_view, name='reply-delete'),

    path('', views.index, name='index1'), ##### !!!!
]











