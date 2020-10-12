from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Spell
from .serializers import SpellSerializer


class SpellList(generics.ListCreateAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer

class SpellDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer