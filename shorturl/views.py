from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework import viewsets
from django.contrib.auth.models import User
from shorturl.models import ShortcutURL
from shorturl.serializers import ShortcutUrlSerializer, UserSerializer, ShortcutUrlRetrieveSerializer
from django.core.exceptions import ObjectDoesNotExist
from shorturl.permissions import IsOwner

# This ViewSet provides 'list' and 'detail' action
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ShortcutUrlsViewSet(viewsets.ModelViewSet):
    queryset = ShortcutURL.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ShortcutUrlRetrieveSerializer
        else:
            return ShortcutUrlSerializer

    permission_classes = [IsOwner, ]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user, numberClick=0)
        else:
            serializer.save()

# Perform the redirection given a shortcut
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