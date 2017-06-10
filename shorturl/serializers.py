from rest_framework import serializers
from shorturl.models import ShortcutURL
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import string
import random

class ShortcutUrlSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    shortcut = serializers.CharField(max_length=7, required=False, validators=[
        RegexValidator(regex=r'^\w{7}$', message='Shortcut must contain 7 digits or letters')])
    numberClick = serializers.ReadOnlyField()

    def create(self, validated_data):
        if not 'shortcut' in validated_data:
            shortcut = ''.join(random.choices(string.ascii_letters+string.digits, k=7))
            while ShortcutURL.objects.filter(shortcut=shortcut):
                shortcut = ''.join(random.choices(string.ascii_letters, k=7))
            validated_data['shortcut'] = shortcut
        return ShortcutURL(**validated_data)

    class Meta:
        model = ShortcutURL
        fields = ('shortcut', 'url', 'title', 'owner', 'numberClick')


class UserSerializer(serializers.ModelSerializer):
    urls = serializers.HyperlinkedRelatedField(many=True, view_name='shortcuturl-detail', read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'urls', 'password')