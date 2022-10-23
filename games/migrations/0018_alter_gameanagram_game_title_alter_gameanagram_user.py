# Generated by Django 4.0.5 on 2022-10-18 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0017_alter_gameanagram_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameanagram',
            name='game_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameanagram', to='games.title'),
        ),
        migrations.AlterField(
            model_name='gameanagram',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gameanagram', to=settings.AUTH_USER_MODEL),
        ),
    ]
