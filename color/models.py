from django.db import models
from spell.models import Spell

class Color(models.Model):
    name = models.CharField(max_length=200)
    hexa = models.CharField(max_length=200)
    spells = models.ManyToManyField(Spell)

def __str__(self):
    return self.name