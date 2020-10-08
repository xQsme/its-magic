"""its_magic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token  
from api.resources import SpellResource
from api.resources import EnemyResource
from api.resources import ColorResource

spell_resource = SpellResource()
enemy_resource = EnemyResource()
color_resource = ColorResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(spell_resource.urls)),
    url(r'^api/', include(enemy_resource.urls)),
    url(r'^api/', include(color_resource.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token)
]
