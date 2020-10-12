# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from color import views

urlpatterns = [
    path('', views.ColorList.as_view()),
    path('<int:pk>/', views.ColorDetail.as_view()),
]