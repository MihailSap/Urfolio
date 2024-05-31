from django.urls import path, include
from .views import Register, profile_management, profile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('profile-management/', profile_management, name='profile-management'),
    path('profile/', profile, name='profile'),
]
