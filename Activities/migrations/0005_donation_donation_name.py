# Generated by Django 2.0.5 on 2018-06-26 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0004_auto_20180625_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donation_name',
            field=models.CharField(default='Donacion', max_length=10),
        ),
    ]