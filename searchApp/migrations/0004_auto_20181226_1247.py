# Generated by Django 2.1.4 on 2018-12-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0003_auto_20181226_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='intake_months',
            field=models.CharField(default='February/July', max_length=100),
        ),
        migrations.AlterField(
            model_name='institute',
            name='is_university',
            field=models.BooleanField(default=True),
        ),
    ]
