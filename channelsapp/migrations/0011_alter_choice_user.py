# Generated by Django 4.0.6 on 2022-07-23 21:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channelsapp', '0010_remove_choice_user_choice_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
