# Generated by Django 3.2.8 on 2021-11-15 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_service_providertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceaddress',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='service.service'),
        ),
    ]