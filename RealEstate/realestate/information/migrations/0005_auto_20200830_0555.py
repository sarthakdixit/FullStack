# Generated by Django 3.0.5 on 2020-08-30 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_interior'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interior',
            old_name='photo1',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='interior',
            name='photo2',
        ),
        migrations.RemoveField(
            model_name='interior',
            name='photo3',
        ),
        migrations.RemoveField(
            model_name='interior',
            name='photo4',
        ),
    ]