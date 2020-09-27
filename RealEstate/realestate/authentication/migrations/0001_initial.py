# Generated by Django 3.0.5 on 2020-08-16 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('online', models.CharField(default='F', max_length=1)),
                ('verified', models.CharField(default='F', max_length=1)),
            ],
        ),
    ]