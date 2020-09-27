# Generated by Django 3.0.5 on 2020-08-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('IDNO', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('typ', models.CharField(max_length=12)),
                ('action', models.CharField(max_length=4)),
                ('localAdd', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=100)),
                ('neigh', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('owner', models.CharField(default='Nothing', max_length=30)),
                ('photo1', models.ImageField(upload_to='buildings/images')),
                ('photo2', models.ImageField(upload_to='buildings/images')),
                ('photo3', models.ImageField(upload_to='buildings/images')),
                ('photo4', models.ImageField(upload_to='buildings/images')),
                ('video', models.FileField(upload_to='buildings/videos')),
            ],
        ),
    ]