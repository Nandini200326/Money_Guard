# Generated by Django 5.2 on 2025-04-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0003_alter_profile_balance_alter_profile_expenses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expenses',
            field=models.FloatField(default=0.0),
        ),
    ]
