# Generated by Django 4.0.5 on 2022-10-18 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0021_alter_gamescore_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamescore',
            old_name='game',
            new_name='title',
        ),
    ]
