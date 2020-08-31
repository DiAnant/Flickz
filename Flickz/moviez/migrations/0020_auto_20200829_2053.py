# Generated by Django 3.1 on 2020-08-29 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0019_auto_20200829_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 29, 15, 23, 30, 991587, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 29, 15, 23, 30, 990592, tzinfo=utc)),
        ),
    ]