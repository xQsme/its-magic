from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User,Group
from .serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework import status
from pprint import pprint

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.order_by('-id')[0]
        user.set_password(user.password)
        group = Group.objects.get(name='USER')
        user.groups.add(group)
        user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED, headers)
        

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if(request.user.id != request.data['id']):
            user = User.objects.filter(id=request.data['id'])[0]
            user.groups.clear()

            for group in request.data['groups']:
                userGroup = Group.objects.get(id=group)
                user.groups.add(userGroup)
            user.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer