from django.db import models
from django.contrib.auth.models import User

# Model to store URL shortcut
class ShortcutURL(models.Model):
    shortcut = models.CharField(max_length=7, primary_key=True)
    title = models.CharField(max_length=40, blank=True)
    url = models.URLField()
    owner = models.ForeignKey(User, related_name='urls', on_delete=models.CASCADE, blank=True)
    numberClick = models.IntegerField(blank=True)