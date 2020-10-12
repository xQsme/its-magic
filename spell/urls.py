# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from spell import views

urlpatterns = [
    path('', views.SpellList.as_view()),
    path('<int:pk>/', views.SpellDetail.as_view()),
]