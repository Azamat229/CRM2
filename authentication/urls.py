from django.urls import path

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
)
app_name = 'authentication'
urlpatterns = [
    path('user', UserRetrieveUpdateAPIView.as_view()),  # Update user's @mail token which get from login request
    path('users', RegistrationAPIView.as_view()),  # Registration a new user
    path('users/login', LoginAPIView.as_view()),  # Login existing user
]