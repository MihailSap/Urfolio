from django.urls import path, include
from .views import Register, profile, profile_management

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('profile-management/', profile_management, name='profile-management'),
    path('profile/<str:username>/', profile, name='profile'),

]
