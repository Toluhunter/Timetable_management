# Generated by Django 3.2.9 on 2021-11-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20211125_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='class_end_time',
        ),
        migrations.RemoveField(
            model_name='table',
            name='class_start_time',
        ),
        migrations.AddField(
            model_name='table',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]