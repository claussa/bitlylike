from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework import viewsets
from django.contrib.auth.models import User
from shorturl.models import ShortcutURL
from shorturl.serializers import ShortcutUrlSerializer, UserSerializer
from django.core.exceptions import ObjectDoesNotExist

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

def redirection(request, **arguments):
    try:
        shortcut = ShortcutURL.objects.get(shortcut=arguments['shortcut'])
    except ObjectDoesNotExist:
        return Http404("Redirection does not exist")
    else:
        print(shortcut.numberClick)
        if shortcut.numberClick is not None:
            shortcut.numberClick += 1
            shortcut.save()
        return redirect(shortcut.url)