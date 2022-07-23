from django.contrib import admin
from .models import Channel, Poll, Choice, Message, UserVote

# Register your models here.
admin.site.register(Channel)
admin.site.register(Poll)
admin.site.register(Message)
admin.site.register(Choice)
admin.site.register(UserVote)

