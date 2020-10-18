# api/urls.py
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.contrib.auth.decorators import permission_required,login_required

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from spell import views

from rest_framework.authentication import TokenAuthentication

urlpatterns = [
    path('', views.SpellList.as_view()),
    path('<int:pk>/', views.SpellDetail.as_view()),
]


@api_view(['GET'])
@authentication_classes((SessionAuthentication, TokenAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def auth_test(request):
    return Response("it's great to have you here with token auth!!")
