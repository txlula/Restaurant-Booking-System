# Generated by Django 2.2.7 on 2020-02-22 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0016_auto_20200221_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='restaurant',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.Restaurant'),
        ),
    ]
