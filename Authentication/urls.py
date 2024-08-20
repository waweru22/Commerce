from django.urls import path
from .views import LoginView, LogoutView, TokenTestView
from . import views

urlpatterns = [
    path('', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('testing/', TokenTestView.as_view())
]