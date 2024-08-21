from . import views
from .views import CartItems
from django.urls import path

urlpatterns = [
    path('items/', CartItems.as_view()),
]