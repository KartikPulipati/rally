from django.db import models

# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=255)
    location = models.IntegerField()

class Poll(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=500)

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice

