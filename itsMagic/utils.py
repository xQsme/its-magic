import json 
from datetime import datetime
from calendar import timegm
#from rest_framework_jwt.settings import api_settings

def jwt_response_payload_handler(token, user=None, request=None):

    l = user.groups.values_list('name',flat = True) # QuerySet Object
    user_roles = list(l)
    """ 
    Custom response payload handler.
    This function controlls the custom payload after login or token refresh. This data is returned through the web API.
    """
    return {
        'token': token,
        'user': {
            'id':user.id,
            'username':user.username,
			'email': user.email,
            'role': user_roles
        }
    }
