from django.db import models
from accounts.models import UserProfile

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)


    created_at = models.DateTimeField(null=True, auto_now_add=True)
    # this date will change every time we update entry
    update_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

class Message(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(null=True, auto_now_add=True)
    # this date will change every time we update entry
    update_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self) -> str:
        return str(self.user.user.email) +' - ' + str(self.room.name)