# Generated by Django 4.0.5 on 2022-10-22 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0024_alter_title_options_rename_title_title_game_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='titles', to=settings.AUTH_USER_MODEL),
        ),
    ]