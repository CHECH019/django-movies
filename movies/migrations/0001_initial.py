# Generated by Django 5.0.4 on 2024-04-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
    ]
