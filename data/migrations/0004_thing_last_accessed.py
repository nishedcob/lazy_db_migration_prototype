# Generated by Django 2.2.7 on 2020-10-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_datetime_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='last_accessed',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
