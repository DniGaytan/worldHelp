# Generated by Django 2.0.1 on 2018-06-27 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0006_auto_20180626_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='activity',
            field=models.ForeignKey(default=42, on_delete=django.db.models.deletion.CASCADE, to='Activities.Activity'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_type',
            field=models.CharField(choices=[('monetario', 'Monetario'), ('recursos', 'Recursos'), ('voluntariado', 'Voluntariado')], default='monetario', max_length=3),
        ),
    ]
