# Generated by Django 3.1 on 2020-08-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0035_auto_20200830_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='timings',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='booking_time',
            field=models.IntegerField(default=1598734613, editable=False),
        ),
    ]