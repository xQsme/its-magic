from tastypie.resources import ModelResource
from api.models import Spell

class SpellResource(ModelResource):
    class Meta:
        queryset = Spell.objects.all()
        resource_name = 'spell'