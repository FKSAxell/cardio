# Generated by Django 2.2.4 on 2019-08-29 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predecir', '0002_auto_20190828_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='date',
            field=models.DateTimeField(default=datetime.date(2019, 8, 28)),
        ),
    ]
