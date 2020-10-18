from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
# Create your views here.
from rest_framework import generics
from .models import Enemy
from .serializers import EnemySerializer


class EnemyList(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = Enemy.objects.order_by('hp')
    serializer_class = EnemySerializer

class EnemyDetail(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser,)
    queryset = Enemy.objects.order_by('hp')
    serializer_class = EnemySerializer