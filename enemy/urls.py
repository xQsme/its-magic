# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from enemy import views

urlpatterns = [
    path('', views.EnemyList.as_view()),
    path('<int:pk>/', views.EnemyDetail.as_view()),
]