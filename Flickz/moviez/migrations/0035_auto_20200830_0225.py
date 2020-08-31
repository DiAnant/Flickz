# Generated by Django 3.1 on 2020-08-29 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0034_auto_20200830_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='Timing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moviez.timing'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='booking_time',
            field=models.IntegerField(default=1598734542, editable=False),
        ),
    ]
