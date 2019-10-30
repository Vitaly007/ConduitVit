from django.urls import path
from django.contrib.auth import views 

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name = 'authentication'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login', LoginAPIView.as_view()),
    path('user', UserRetrieveUpdateAPIView.as_view()),
]