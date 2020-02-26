# Generated by Django 2.2.7 on 2020-02-25 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0033_auto_20200225_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='staff',
            name='restaurant',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.Restaurant'),
        ),
    ]