# Generated by Django 4.0.5 on 2022-11-01 01:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0027_alter_contactus_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]