# Generated by Django 2.2.7 on 2019-12-09 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20191209_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='person',
        ),
    ]
