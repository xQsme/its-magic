# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.contrib.auth.decorators import permission_required,login_required
from rest_framework.authentication import TokenAuthentication


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def auth_test(request):
    return Response("it's great to have you here with token auth!!")

@api_view(['GET'])
def free_test(request):
    #print(request.META['HTTP_AUTHORIZATION'])
    return Response("entry without token auth !!")