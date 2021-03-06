# Generated by Django 3.2.4 on 2022-01-28 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_alter_flyer_event_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flyer_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flyer_image', models.ImageField(upload_to='flyer_imgs/')),
            ],
        ),
        migrations.RemoveField(
            model_name='flyer',
            name='id',
        ),
        migrations.AlterField(
            model_name='flyer',
            name='Flyer_image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainApp.flyer_image'),
        ),
    ]
