# Generated by Django 3.1 on 2020-08-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0022_auto_20200829_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='phone',
            field=models.IntegerField(max_length=12),
        ),
    ]