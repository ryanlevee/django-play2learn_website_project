# Generated by Django 4.0.5 on 2022-10-18 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0008_rename_created_gamescore_timestamp_gamescore_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamescore',
            name='title',
        ),
        migrations.RemoveField(
            model_name='gamescore',
            name='user',
        ),
    ]