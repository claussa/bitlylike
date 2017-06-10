from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from shorturl.models import ShortcutURL
from shorturl.serializers import ShortcutUrlSerializer, UserSerializer

# This ViewSet provides 'list' and 'detail' action
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #TODO Add permission

class ShortcutUrlsViewSet(viewsets.ModelViewSet):
    queryset = ShortcutURL.objects.all()
    serializer_class = ShortcutUrlSerializer
    #TODO Add permission

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user, numberClick=0)
        else:
            serializer.save()