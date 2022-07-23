from django.db import models
from authUser.models import Member


class Petition(models.Model):
    created_by = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1500)

    def __str__(self):
        return self.name + " " + self.email + " " + self.message


class Signature(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.petition.name} - {self.member.last_name}'
