# Generated by Django 2.2.7 on 2020-02-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0032_auto_20200225_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='staff',
        ),
        migrations.AddField(
            model_name='staff',
            name='restaurant',
            field=models.ManyToManyField(to='bookings.Restaurant'),
        ),
    ]
