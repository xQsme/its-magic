# api/serializers.py
from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'xp', 'currentXP', 'hp', 'currentHP', 'mana', 'currentMana', 'damage', 'image', 'sound')