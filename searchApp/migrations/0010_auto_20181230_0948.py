# Generated by Django 2.1.4 on 2018-12-30 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0009_remove_institute_location'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='institute',
            unique_together={('name', 'country')},
        ),
    ]