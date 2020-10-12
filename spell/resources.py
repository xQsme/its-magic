from tastypie.resources import ModelResource
from api.models import Spell
from tastypie.authorization import Authorization

class SpellResource(ModelResource):
    class Meta:
        queryset = Spell.objects.all()
        resource_name = 'spell'
        authorization = Authorization()