# Generated by Django 4.2.13 on 2024-06-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efficiency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionlog',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
