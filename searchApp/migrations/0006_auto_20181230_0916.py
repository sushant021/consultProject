# Generated by Django 2.1.4 on 2018-12-30 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0005_auto_20181226_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(default='4 Years', max_length=200),
        ),
    ]