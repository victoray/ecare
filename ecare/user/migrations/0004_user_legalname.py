# Generated by Django 3.2.8 on 2021-11-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20211114_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='legalName',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Legal Name'),
        ),
    ]
