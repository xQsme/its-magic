from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Enemy
from .serializers import EnemySerializer


class EnemyList(generics.ListCreateAPIView):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer

class EnemyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer