from django.urls import path, include
from .views import Register


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #path('', include(), name='home'),
    #path('', include('main.urls'), name='main'),
    path('register/', Register.as_view(), name='register'),
]
