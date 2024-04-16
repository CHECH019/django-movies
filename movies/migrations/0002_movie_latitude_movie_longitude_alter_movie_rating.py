# Generated by Django 5.0.4 on 2024-04-16 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
