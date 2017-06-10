from rest_framework import serializers
from shortUrl.models import ShortcutURL
from django.contrib.auth.models import User

class ShortcutUrlSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = ShortcutURL
        fields = ('shortcut', 'url', 'title', 'owner', 'numberClick')

class UserSerializer(serializers.ModelSerializer):
    urls = serializers.PrimaryKeyRelatedField(many=True, queryset=ShortcutURL.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'urls')