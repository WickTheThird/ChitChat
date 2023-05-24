from django.db import models
from django.contrib.auth.models import User
from django import forms

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password1 = models.CharField(max_length=50, blank=True)
    password2 = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["name"]
    
    def __str__(self) -> str:
        return self.name


class Friends(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_friends')
    friends = models.ManyToManyField(Users, related_name='user_friendship')

    requestsSent = models.ManyToManyField(Users, related_name='requests_sent')
    requestsReceived = models.ManyToManyField(Users, related_name='requests_received')

    class Meta:
        ordering = ["user"]

    def addUser(self, userID):
        self.friends.add(userID)

    def remove(self, userID):
        self.friends.filter(userID == userID).delete()

    def search(self, userName):
        return self.friends.filter(users__name=userName)
    
    def reqSent(self, toUser):
        self.requestsSent.add(toUser)

    def reqReceived(self, fromUser):
        self.reqReceived.add(fromUser)

    def __str__(self) -> list:
        return [x for x in self.friends.all()]


class FriendRequest(models.Model):
    reciever = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_reciever')
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_sender')

    status = {
        0 : "sent",
        1 : "received",
        2 : "accepted",
        3 : "rejected",
    }
    
    def state(self, stateID) -> str:
        return self.status[stateID]

    def addRequest(self): # note that this adds requests both sent and recieved
        self.reciever.reqReceived(self.sender)
        self.sender.reqSent(self.reciever)

    def __str__(self) -> str:
        return self.state()
