# Generated by Django 3.1 on 2020-08-29 10:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0015_auto_20200829_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 29, 10, 10, 48, 668448, tzinfo=utc)),
        ),
    ]