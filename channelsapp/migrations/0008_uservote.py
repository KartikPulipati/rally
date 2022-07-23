# Generated by Django 4.0.6 on 2022-07-23 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channelsapp', '0007_alter_message_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channelsapp.poll')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
