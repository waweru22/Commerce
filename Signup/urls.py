from django.urls import path
from .views import Users
from . import views

urlpatterns = [
    path('', views.getData),
    # path('add_user/', views.addUser),
    path('users/', Users.as_view()),
]