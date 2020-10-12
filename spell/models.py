from django.db import models

# Create your models here.
class Spell(models.Model):
    name = models.CharField(max_length=200)
    damage = models.PositiveIntegerField(default = 0)
    image = models.ImageField(upload_to ='uploads/',default = '')

def __str__(self):
    return self.name