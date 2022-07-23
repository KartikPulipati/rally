from django.contrib import admin
from .models import Channel, Poll, Choice

# Register your models here.
admin.site.register(Channel)
admin.site.register(Poll)
admin.site.register(Choice)

