# Generated by Django 4.0.1 on 2022-01-18 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_alter_flyer_flyer_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flyer',
            old_name='Date',
            new_name='Event_date',
        ),
    ]
