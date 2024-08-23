from . import views
from .views import CartItemView
from django.urls import path

urlpatterns = [
    path('', views.getCartData),
    path('items/', views.getCartItemData),
    path('additems/', CartItemView.as_view()),
]