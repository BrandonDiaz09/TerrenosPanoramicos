# Generated by Django 3.1.4 on 2021-01-04 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210103_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_nameMa',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
