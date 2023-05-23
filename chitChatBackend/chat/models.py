from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self) -> str:
        return self.name


class Friends(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_friends')
    friends = models.ManyToManyField(Users, related_name='user_friendship')
    
    def addUser(self, userID):
        self.friends.add(userID)
    
    def remove(self, userID):
        self.friends.remove(userID)

    def search(self, userName):
        return self.friends.filter(users__name=userName)

    def __str__(self) -> list:
        return [x for x in self.friends.all()]
