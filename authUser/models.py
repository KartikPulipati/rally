from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models
from channelsapp.models import Channel


class Member(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    is_mod = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name + " " + self.last_name