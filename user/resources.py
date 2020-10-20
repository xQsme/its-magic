from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie.authorization import Authorization

class PlayerResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()