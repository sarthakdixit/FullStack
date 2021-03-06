# Generated by Django 3.0.5 on 2020-08-26 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_buildings_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('owner', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(default='null', max_length=30)),
                ('email', models.CharField(default='null', max_length=30)),
                ('number', models.CharField(default='null', max_length=30)),
                ('add', models.CharField(default='null', max_length=30)),
                ('city', models.CharField(default='null', max_length=30)),
                ('state', models.CharField(default='null', max_length=30)),
                ('about', models.CharField(default='null', max_length=100)),
                ('licence', models.CharField(default='null', max_length=15)),
                ('date', models.CharField(default='null', max_length=15)),
                ('photo', models.ImageField(upload_to='agents')),
            ],
        ),
    ]
