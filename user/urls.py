# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UseDetail.as_view()),
]