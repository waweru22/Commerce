from django.urls import path
from .views import LoginView
from . import views

urlpatterns = [
    path('', LoginView.as_view()),
]