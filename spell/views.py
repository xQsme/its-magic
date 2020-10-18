from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
# Create your views here.
from rest_framework import generics
from .models import Spell
from .serializers import SpellSerializer


class SpellList(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer

class SpellDetail(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser,)
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer