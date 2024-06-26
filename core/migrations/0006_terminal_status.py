# Generated by Django 4.2.10 on 2024-04-18 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_deviceinfo_device_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminal',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('faulty', 'Faulty'), ('retrieved', 'Retrieved'), ('deployed', 'Deployed')], default='active', max_length=20),
        ),
    ]
