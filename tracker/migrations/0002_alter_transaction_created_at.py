# Generated by Django 5.2.1 on 2025-05-17 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
