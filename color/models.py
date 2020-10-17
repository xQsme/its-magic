from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=200)
    hexa = models.CharField(max_length=200)

def __str__(self):
    return self.name