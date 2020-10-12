from tastypie.resources import ModelResource
from api.models import Enemy
from tastypie.authorization import Authorization

class EnemyResource(ModelResource):
    class Meta:
        queryset = Enemy.objects.all()
        resource_name = 'enemy'
        authorization = Authorization()