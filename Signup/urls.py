from django.urls import path
from .views import UserRegistration
from . import views

urlpatterns = [
    path('', views.getData),
    # path('add_user/', views.addUser),
    path('user/', UserRegistration.as_view()),
]