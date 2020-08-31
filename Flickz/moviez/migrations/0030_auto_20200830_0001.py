# Generated by Django 3.1 on 2020-08-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0029_auto_20200830_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='booked_time',
        ),
        migrations.AddField(
            model_name='ticket',
            name='expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='booking_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
