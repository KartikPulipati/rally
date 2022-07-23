from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models
from channelsapp.models import Channel


class Member(AbstractUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, max_length=255)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    is_mod = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    FIRST_NAME_FIELD = "first_name"
    LAST_NAME_FIELD = "last_name"

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + " " + self.last_name
