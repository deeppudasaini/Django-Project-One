# Generated by Django 2.2.13 on 2021-05-25 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210525_0918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firstName',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lastName',
            new_name='lastname',
        ),
    ]
