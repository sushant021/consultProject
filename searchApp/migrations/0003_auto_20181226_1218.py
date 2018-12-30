# Generated by Django 2.1.4 on 2018-12-26 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0002_auto_20181226_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='intake_months',
            field=models.CharField(default='Feb/Jan', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='institute',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
