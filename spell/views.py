from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Spell
from .serializers import SpellSerializer
from pprint import pprint
from rest_framework import status


class SpellList(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    
    def create(self, request, *args, **kwargs):
        request.data['colors'] = request.data['colors'].split(',')
        request.data['colors'] = [int(i, base=16) for i in request.data['colors']]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        spell = Spell.objects.order_by('-id')[0]
        for color in request.data['colors']:
            spell.colors.add(color)
        spell.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED, headers)

class SpellDetail(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser,)
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        colors = request.data['colors'].split(',')
        colors = [int(i, base=16) for i in colors]

        spell = Spell.objects.filter(id=request.data['id'])[0]

        for color in colors:
            spell.colors.add(color)
        spell.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)