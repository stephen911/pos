# Generated by Django 4.2.10 on 2024-04-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_monitor_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='zone',
            field=models.CharField(choices=[('zone1', 'Zone1'), ('zone2', 'Zone2'), ('zone3', 'Zone3')], default='zone1', max_length=20),
        ),
    ]
