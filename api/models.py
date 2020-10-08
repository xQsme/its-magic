from django.db import models

# Create your models here.
class Spell(models.Model):
    name = models.CharField(max_length=200)
    damage = models.PositiveIntegerField
    image = models.ImageField
    color = models.CharField(max_length=200)

class Enemy(models.Model):
    name = models.CharField(max_length=200)
    life = models.PositiveIntegerField
    image = models.ImageField(upload_to ='uploads/')
    
    
class Color(models.Model):
    name = models.CharField(max_length=200)
    hexa = models.CharField(max_length=200)

def __str__(self):
    return self.name