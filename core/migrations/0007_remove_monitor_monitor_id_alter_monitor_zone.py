# Generated by Django 4.2.10 on 2024-04-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_terminal_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='monitor_id',
        ),
        migrations.AlterField(
            model_name='monitor',
            name='zone',
            field=models.CharField(choices=[('zone 1', 'Zone 1'), ('zone 2', 'Zone 2'), ('zone 3', 'Zone 3')], default='zone 1', max_length=100),
        ),
    ]
