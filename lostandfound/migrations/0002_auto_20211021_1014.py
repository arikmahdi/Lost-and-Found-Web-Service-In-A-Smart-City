# Generated by Django 3.2.6 on 2021-10-21 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lostandfound', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lostpet',
            name='breed_lost',
        ),
        migrations.RemoveField(
            model_name='lostpet',
            name='color_lost',
        ),
    ]
