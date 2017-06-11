from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework import viewsets
from django.contrib.auth.models import User
from shorturl.models import ShortcutURL
from shorturl.serializers import ShortcutUrlSerializer, UserSerializer, ShortcutUrlRetrieveSerializer
from django.core.exceptions import ObjectDoesNotExist
from shorturl.permissions import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    """
    This ViewSet provides 'list', 'retrieve' and 'create' action for Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShortcutUrlsViewSet(viewsets.ModelViewSet):
    """
    This ViewSet provides 'list', 'create', 'retrieve', 'update' and 'delete' action for Shortcut
    """
    queryset = ShortcutURL.objects.all()
    permission_classes = [IsOwner]

    # Set a different serializer for the 'retrieve' action allowing to see statistics
    def get_serializer_class(self):
        print(self.action)
        if self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            return ShortcutUrlRetrieveSerializer
        else:
            return ShortcutUrlSerializer

    # Before the creation of a new Shortcut, if the user is authenticated the owner of the shortcut is set
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user, numberClick=0)
        else:
            serializer.save()


def redirection(request, **arguments):
    """
    Perform the redirection given a shortcut
    """
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