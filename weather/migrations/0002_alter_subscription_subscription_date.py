# Generated by Django 4.2.3 on 2023-08-19 10:17

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscription_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 10, 17, 49, 555865, tzinfo=datetime.UTC)),
        ),
    ]