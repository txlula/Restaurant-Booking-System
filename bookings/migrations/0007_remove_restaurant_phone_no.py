# Generated by Django 2.2.7 on 2020-01-30 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_auto_20191224_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='phone_no',
        ),
    ]
