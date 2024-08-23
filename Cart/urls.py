from . import views
from .views import CartItemView
from django.urls import path

urlpatterns = [
    path('', views.get_cart_data),
    path('items/', views.get_cart_item_data),
    path('removeitem/<int:item_id>/', views.delete_cart_item),
    path('additems/', CartItemView.as_view()),
]