# Generated by Django 3.2.8 on 2021-11-14 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0001_initial'),
        ('user', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dateOfBirth',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emergencyContact',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default=None, max_length=255, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='governmentId',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profileImage',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='role.role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email address'),
        ),
    ]
