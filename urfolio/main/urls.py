from django.contrib import admin
from django.urls import path, include
from . import views
from .views import (
    ProjectListView, ProjectCreateView,
    ProjectDetailView, ProjectUpdateView,
    ProjectDeleteView, LikeView
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('new/', ProjectCreateView.as_view(), name='project_create'),
    path('like/<int:pk>', LikeView, name='like_project'),

    # Фильтры - нужны?
    #path('', views.index, name='index'),
    #path('category/<int:category_id>/', views.index, name='category'),
    #path('category/<int:year_id>/', views.index, name='year'),
    #path('category/<int:course_number_id>/', views.index, name='course_number'),
]










