from django.contrib.auth.models import User
from django.db import models

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username







