# api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import Group,User

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('id', 'name',)

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email','groups',)