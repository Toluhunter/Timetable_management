# Generated by Django 3.2.9 on 2021-11-27 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_delete_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.lecturer')),
            ],
        ),
    ]
