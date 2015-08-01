from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()

from rest_framework import permissions, routers, serializers, viewsets

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^v1/', include(router.urls)),
    url(r'^v1/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)

