# Generated by Django 2.2.2 on 2019-06-22 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potHole', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pothole',
            old_name='inchesDeep',
            new_name='inches_Deep',
        ),
    ]