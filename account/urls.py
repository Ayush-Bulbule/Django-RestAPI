from django.contrib import admin
from django.urls import path
from account.views import LoginView, RegisterView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view())
]
