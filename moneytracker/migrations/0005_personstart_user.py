# Generated by Django 3.0.2 on 2020-02-01 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moneytracker', '0004_auto_20200131_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='personstart',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
