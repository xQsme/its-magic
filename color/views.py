from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Color
from .serializers import ColorSerializer


class ColorList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class ColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer