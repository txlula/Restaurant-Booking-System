# Generated by Django 2.2.7 on 2020-02-03 20:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_auto_20200203_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='person',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bookings.Person'),
        ),
        migrations.AlterField(
            model_name='order',
            name='dish',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bookings.Dish'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_of_booking',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
