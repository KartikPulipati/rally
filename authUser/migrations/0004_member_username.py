# Generated by Django 4.0.6 on 2022-07-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authUser', '0003_remove_member_username_alter_member_channel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
