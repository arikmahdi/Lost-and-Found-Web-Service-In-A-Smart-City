# Generated by Django 3.2.6 on 2021-10-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostandfound', '0002_auto_20211021_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostpet',
            name='picture_lost',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Image'),
        ),
    ]