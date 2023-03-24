from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    friends = models.ManyToManyField(User, blank=True,related_name='friends')
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name

class FriendRequests(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender', null=True)
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='receiver', null=True)

    state = models.BooleanField(blank=True)

    def __str__(self):

        if self.state:
            return self.sender.name + " -> " + self.receiver.name + " (pending)"
        else:
            return "Request Processed" 
