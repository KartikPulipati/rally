from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authUser.models import Member

admin.site.register(Member, UserAdmin)
