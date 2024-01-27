from django.db import models
from django.utils.translation import gettext_lazy as _
from auth_system.models import CustomUser

# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Add other fields specific to the UserProfile
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    # this date will change every time we update entry
    update_at = models.DateTimeField(null=True, auto_now=True)


    def __str__(self) -> str:
        return str(self.id)+" - "+ str(self.user.first_name) if self.user.first_name != None else str(self.id)




