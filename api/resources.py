from tastypie.resources import ModelResource
from api.models import Spell
from api.models import Enemy
from api.models import Color
from tastypie.authorization import Authorization

class SpellResource(ModelResource):
    class Meta:
        queryset = Spell.objects.all()
        resource_name = 'spell'
        authorization = Authorization()

class EnemyResource(ModelResource):
    class Meta:
        queryset = Enemy.objects.all()
        resource_name = 'enemy'
        authorization = Authorization()

class ColorResource(ModelResource):
    class Meta:
        queryset = Color.objects.all()
        resource_name = 'color'
        authorization = Authorization()