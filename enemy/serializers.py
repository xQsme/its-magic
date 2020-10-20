# api/serializers.py
from rest_framework import serializers
from .models import Enemy

class EnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemy
        fields = ('id', 'name', 'xp', 'hp', 'currentHP', 'mana', 'currentMana', 'damage', 'image', 'sound')