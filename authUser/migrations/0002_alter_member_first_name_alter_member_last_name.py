# Generated by Django 4.0.6 on 2022-07-23 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]
