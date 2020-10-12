from tastypie.resources import ModelResource
from api.models import Color
from tastypie.authorization import Authorization

class ColorResource(ModelResource):
    class Meta:
        queryset = Color.objects.all()
        resource_name = 'color'
        authorization = Authorization()