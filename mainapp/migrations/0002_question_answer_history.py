# Generated by Django 5.0.4 on 2024-04-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_history',
            field=models.JSONField(default=dict, verbose_name='Answers History'),
        ),
    ]