from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
# Create your views here.
from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer


class PlayerList(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = Player.objects.order_by('xp')
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser,)
    queryset = Player.objects.order_by('xp')
    serializer_class = PlayerSerializer