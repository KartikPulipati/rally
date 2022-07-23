from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models
from channelsapp.models import Channel


class Member(AbstractUser, PermissionsMixin):
    username = models.EmailField(unique=True, null=True)
    email = models.EmailField('email address', unique=True, max_length=255)
    first_name = models.CharField("first name", max_length=150)
    last_name = models.CharField("last name", max_length=150)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    is_mod = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username", 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name
