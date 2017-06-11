from rest_framework import serializers
from shorturl.models import ShortcutURL
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from rest_framework.validators import UniqueValidator
import string
import random

class ShortcutUrlRetrieveSerializer(serializers.ModelSerializer):
    """
    Serializer to 'retrieve' and 'update' shortcut
        Allow to see statistics, the owner
        Allow to only update the title of the shortcut
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    shortcut = serializers.ReadOnlyField()
    numberClick = serializers.ReadOnlyField()
    url = serializers.ReadOnlyField()

    class Meta:
        model = ShortcutURL
        fields = ('shortcut', 'url', 'title', 'owner', 'numberClick')

class ShortcutUrlSerializer(serializers.ModelSerializer):
    """
    Serializer to 'list', 'create' and 'delete' shortcut
        Allow to see the shortcut, url and title only
        Validate the form of the shortcut (7 letters or digits)
    """
    shortcut = serializers.CharField(max_length=7, required=False, validators=[
        RegexValidator(regex=r'^\w{7}$', message='Shortcut must contain 7 digits or letters'),
        UniqueValidator(queryset=ShortcutURL.objects.all(),
            message="This shortcut is already used. Choose an another shortcut or leave blank to obtain a random shortcut.")])

    # Verify if the shortcut is set, if not set a random shortcut
    def create(self, validated_data):
        if not 'shortcut' in validated_data:
            shortcut = ''.join(random.choices(string.ascii_letters+string.digits, k=7))
            while ShortcutURL.objects.filter(shortcut=shortcut):
                shortcut = ''.join(random.choices(string.ascii_letters, k=7))
            validated_data['shortcut'] = shortcut
        return ShortcutURL.objects.create(**validated_data)

    class Meta:
        model = ShortcutURL
        fields = ('shortcut', 'url', 'title')    


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user model
        Allow to see all the shortcut of associate to a user
        Allow to create new user
    """
    urls = serializers.HyperlinkedRelatedField(many=True, view_name='shortcuturl-detail', read_only=True)
    password = serializers.CharField(write_only=True)

    # Hash the password to create a new user
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'urls', 'password')