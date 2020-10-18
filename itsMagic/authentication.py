from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class JSONWebTokenAuthenticationQS(JSONWebTokenAuthentication):
   def get_jwt_value(self, request):
        return request.GET.get('jwt') or JSONWebTokenAuthentication.get_jwt_value(self, request)