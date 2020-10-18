# api/serializers.py
from rest_framework import serializers
from .models import Spell
from color.serializers import ColorSerializer

class SpellSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(read_only=True, many=True)

    class Meta:
        model = Spell
        fields = ('id', 'name', 'damage', 'image', 'colors')