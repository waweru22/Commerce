from . import views
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('product/', views.ProductAPI.as_view()),
    path('getprod/', views.getProducts),
    path('category/', views.CategoryAPI.as_view()),
    path('image/', views.ImageAPI.as_view())
    ]