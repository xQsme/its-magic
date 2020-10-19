# api/serializers.py
from rest_framework import serializers
from .models import Spell
from color.serializers import ColorSerializer
from color.models import Color

class SpellSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)
    # colors = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(), many=True)
    class Meta:
        model = Spell
        fields = ('id', 'name', 'damage', 'image', 'colors')
