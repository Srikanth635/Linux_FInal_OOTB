# Generated by Django 3.0.4 on 2020-05-25 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0015_auto_20200525_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configkeyvaluestorage',
            name='config_type',
        ),
    ]