# Generated by Django 5.0.4 on 2024-04-14 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='country_code',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.country', verbose_name='Country Code'),
        ),
    ]
