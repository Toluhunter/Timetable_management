# Generated by Django 3.2.9 on 2021-11-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_lecturer_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='initial',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]
