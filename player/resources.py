from tastypie.resources import ModelResource
from api.models import Player
from tastypie.authorization import Authorization

class PlayerResource(ModelResource):
    class Meta:
        queryset = Player.objects.all()
        resource_name = 'player'
        authorization = Authorization()