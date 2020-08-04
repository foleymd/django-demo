# Generated by Django 3.0.2 on 2020-02-01 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200131_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='investments_start',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Investments up until now.', max_digits=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='savings_start',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Savings up until now.', max_digits=10),
        ),
    ]