# Generated by Django 4.0.6 on 2022-07-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channelsapp', '0002_alter_channel_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='location',
            field=models.IntegerField(),
        ),
    ]
