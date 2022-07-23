from django.db import models
from django.conf import settings


class Channel(models.Model):
    name = models.CharField(max_length=255)
    location = models.IntegerField()

    def __str__(self):
        return self.name

class Message(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return self.message

class Poll(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.channel.name} - {self.pk}'


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice

class UserVote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} voted for {self.poll.prompt}'

