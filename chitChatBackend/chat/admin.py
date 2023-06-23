from django.contrib import admin
from . import models

admin.site.register(models.Users)
admin.site.register(models.Friends)
admin.site.register(models.FriendRequest)
admin.site.register(models.Messages)
