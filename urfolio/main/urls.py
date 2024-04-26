from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('category/<int:category_id>/', views.index, name='category'),
    path('category/<int:year_id>/', views.index, name='year'),
    path('category/<int:course_number_id>/', views.index, name='course_number'),
]
